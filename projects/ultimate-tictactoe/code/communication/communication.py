import socket
import hashlib
import os
import sys


def quit_program():
    '''Quit the program and restart'''
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def get_ip():
    '''Get the machine's IP'''
    hostname = socket.gethostname() 
    ip_address = socket.gethostbyname(hostname)
    return ip_address

def correct_format(splitted_request):
    '''Verify if the received TCP message has the correct format'''
    REQUEST_LIST=['CONNECTION','PLAY','ACK','WIN','END','NEW_STATE','404','405','406']
    PLAY_LIST = [(str(i)+str(j)) for i in range(9) for j in range(9)] # All possible slots in the grid
    if splitted_request[0]!='UTTT/1.0' or len(splitted_request)<2:
        return False
    if not splitted_request[1] in REQUEST_LIST:
        return False
    if splitted_request[1]=='CONNECTION' and len(splitted_request)==2:
        return False
    if splitted_request[1]=='RECONNECTION' and len(splitted_request)==2:
        return False
    if splitted_request[1]=='PLAY':
        if len(splitted_request)<4:
            return False
        if splitted_request[2] not in PLAY_LIST:
            return False
    if splitted_request[1]=='NEW_STATE' and len(splitted_request)<3:
        return False
    if splitted_request[1]=='404' and len(splitted_request)<5:
        return False
    if splitted_request[1]=='WIN':
        if len(splitted_request)>3:
            return False
        if len(splitted_request) == 3:
            if splitted_request[2]!='HOST' and splitted_request[2]!='GUEST':
                return False
    return True

def host_game(IP, PORT, host_pseudo):
    '''Connect with another player as host and starts communication'''
    ### Create socket and wait for connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP,PORT))
    s.listen(1)
    conn, addr = s.accept()
    ### Receive connection
    data = conn.recv(1024)
    message = data.decode()
    split = message.split()
    ### Verify format
    if not correct_format(split) or split[1]!='CONNECTION':
        bad_request(conn)
    ### Send connection   
    message = 'UTTT/1.0 CONNECTION ' + host_pseudo +'\n'
    conn.sendall(message.encode())
    return conn  

def guest_game(IP, PORT, guest_pseudo):
    '''Connect with other player as guest and starts communication'''
    ### Create socket and connect
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    ### Send connection
    message = 'UTTT/1.0 CONNECTION ' + guest_pseudo + '\n'
    s.sendall(message.encode())
    ### Receive connection
    data = s.recv(1024)      
    message = data.decode()
    split = message.split()
    ### Handle error and verify format
    if not correct_format(split) or split[1]!='CONNECTION':
        bad_request(s)
    handle_error(split, s)
    return s

def convert_to_string(global_board):
    '''Convert the global board into the state of play defined in the protocol'''
    string = ''
    for i in range(9):
        small_board = global_board.local_board_list[i]
        for j in range(3):
            for k in range(3):
                slot = small_board.board[j][k]
                if slot == 0:
                    string += '.'
                elif slot == 1:
                    string += '1'
                else:
                    string += '0'
        if i in [2,5]:
            string += '/'
        elif i in [0,1,3,4,6,7]:
            string += '-'
    return string

def close_connection(sock):
    '''Close the connection call quit_program'''
    sock.close()
    quit_program()  

def handle_error(splitted_request, sock):
    '''Verify if we receive an error'''
    if splitted_request[1]=='405' or splitted_request[1]=='406':
        close_connection(sock)

def bad_request(sock):
    '''Send a bad request error'''
    message = 'UTTT/1.0 405 BAD_REQUEST\n'
    sock.sendall(message.encode())
    close_connection(sock)

def fatal_error(sock):
    message = 'UTTT/1.0 406 FATAL_ERROR\n'
    sock.sendall(message.encode())
    close_connection(sock)

def update_sop(state_of_play, play, turn):
    '''Update the state of play with a move'''
    big_slot = int(play[0])
    small_slot = int(play[1])
    index = big_slot*10+small_slot
    if turn==1:
        move = 1
    else:
        move = 0
    return state_of_play[:index] + str(move) + state_of_play[index+1:]

def hash(string):
    string_hashed = hashlib.sha3_224(string.encode()).hexdigest()
    return string_hashed

def get_play(sock, state_of_play, turn):
    '''Handle communication when its opponent's turn'''
    ### Receive play
    data = sock.recv(1024)
    message = data.decode()
    split = message.split()
    ### Handle error and verify format
    if not correct_format(split) or split[1]!='PLAY':
        bad_request(sock)
    handle_error(split, sock)
    ### Send new state
    play = split[2]
    new_state = update_sop(state_of_play, play, turn)
    new_state_hashed = hash(new_state)
    message = 'UTTT/1.0 NEW_STATE ' + new_state_hashed + '\n'
    sock.sendall(message.encode())
    ### Receive response
    data = sock.recv(1024)
    message = data.decode()
    split = message.split()
    ### Handle error and verify format
    if not correct_format(split):
        bad_request(sock)
    handle_error(split, sock)
    ### Receive ack
    if split[1]=='ACK':
        return play
    elif split[1]=='404':
        play = split[3]
        new_state = update_sop(state_of_play, play, turn)
        new_state_hashed = hash(new_state)
        message = 'UTTT/1.0 NEW_STATE ' + new_state_hashed + '\n'
        sock.sendall(message.encode())
        ### Receive response
        data = sock.recv(1024)
        message = data.decode()
        split = message.split()
        ### Handle error and verify format
        if not correct_format(split):
            bad_request(sock)
        handle_error(split, sock)
        if split[1] == 'ACK':
            return play
        else :
            close_connection(sock)
    else:
        bad_request(sock)

def send_play(sock, play, state_of_play, turn):
    '''Handle communication when it's local player's turn'''
    ### Send play
    sop_hashed = hash(str(state_of_play))
    message = 'UTTT/1.0 PLAY ' + play + ' ' + sop_hashed + '\n'
    sock.sendall(message.encode())    
    ### Receive response
    new_state = update_sop(state_of_play, play, turn)
    new_state_hashed = hash(new_state)
    data = sock.recv(1024)
    message = data.decode()
    split = message.split()
    ### Handle error and verify format
    if not correct_format(split) or split[1]!='NEW_STATE':
        bad_request(sock)
    handle_error(split, sock)
    ### Send ack
    rcv_sop_hashed = split[2]
    if rcv_sop_hashed == new_state_hashed:
        message = 'UTTT/1.0 ACK\n'
        sock.sendall(message.encode())
    ### State play error
    else :
        message = 'UTTT/1.0 404 STATE_PLAY ' + play + ' ' + sop_hashed + '\n'
        sock.sendall(message.encode())
        ### Receive response
        data = sock.recv(1024)
        message = data.decode()      
        split = message.split()
        ### Handle error and verify format
        if not correct_format(split) or split[1]!='NEW_STATE':
            bad_request(sock)
        handle_error(split, sock)
        ### Send ack
        rcv_sop_hashed = split[2]
        if rcv_sop_hashed == new_state_hashed:
            message = 'UTTT/1.0 ACK\n'
            sock.sendall(message.encode())
        ### Fatal error
        else:
            fatal_error(sock)

def end_game(sock, turn, player, bot, prev_turn):
    '''Handle connection when the game is over'''
    if player == None:
        player = bot
    if turn == 0: # Draw
        if prev_turn == player : # We played last
            ### Receive DRAW
            data = sock.recv(1024)
            message = data.decode()
            split = message.split()
            ### Verify format, request and draw
            if not correct_format(split):
                bad_request(sock)
            if split[1]!='WIN' or len(split)>2 :
                fatal_error(sock)
            ### Send END
            else :
                message = 'UTTT/1.0 END\n'
                sock.sendall(message.encode())
                close_connection(sock)
        else : # Opponent played last
            ### Send DRAW
            message = 'UTTT/1.0 WIN\n'
            sock.sendall(message.encoede())
            ### Receive END
            data = sock.recv(1024)
            message = data.decode()
            split = message.split()
            ### Verify format, end
            if not correct_format(split):
                bad_request(sock)
            handle_error(split, sock)
            if split[1] != 'END':
                bad_request(sock)
            else :
                close_connection(sock)
    else :
        if turn == player : # We won
            ### Receive WIN
            data = sock.recv(1024)
            message = data.decode()
            split = message.split()
            ### Verify format, request and winner
            if not correct_format(split):
                bad_request(sock)
            handle_error(split, sock)
            if split[1] != 'WIN' or len(split)<3:
                fatal_error(sock)
            else :
                if (split[2]=='HOST' and player==1) or (split[2]=='GUEST' and player==2):
                    fatal_error(sock)
                else : # Send END
                    message = 'UTTT/1.0 END\n'
                    sock.sendall(message.encode())
                    close_connection(sock)
        else : # We lost
            ### Send WIN
            if player == 1 : # Player is GUEST
                message = 'UTTT/1.0 WIN HOST\n'
            else : # Player is HOST
                message = 'UTTT/1.0 WIN GUEST\n'
            sock.sendall(message.encode())
            ### Receive END
            data = sock.recv(1024)
            message = data.decode()
            split = message.split()
            ### Verify format and errors
            if not correct_format(split):
                bad_request(sock)
            handle_error(split, sock)
            close_connection(sock)
