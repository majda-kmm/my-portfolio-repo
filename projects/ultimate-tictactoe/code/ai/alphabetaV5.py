from math import inf
from collections import Counter

#all the ways to have a tic tac toe
#diagonale
possible_goals = [([0,0],[1,1] , [2,2]), ([0,2], [1,1], [2,0])]
#colomn
possible_goals += [([0,i], [1,i], [2,i]) for i in range(3)]
#row
possible_goals += [([i,0], [i,1], [i,2]) for i in range(3)]

def next_box(last_move):
    #find the local board in which we will play depend on the adversary move
    return (last_move[1]*3)+last_move[2]

def check_box(box_str):
    #check if we have a tic tac toe in the board (local or global)
    global possible_goals
    for idxs in possible_goals:
        (x, y, z) = idxs
        if (box_str[x[0]][x[1]] == box_str[y[0]][y[1]] == box_str[z[0]][z[1]]) and box_str[x[0]][x[1]] !=0:
            return box_str[x[0]][x[1]]
    return 0


def possible_moves(state,last_move,box_won):
    #find all the possibles moves the IA can do 
    possible_indices = []
    box_to_play = next_box(last_move)
    if box_won[box_to_play//3][box_to_play%3] !=0:
        for i in range(9):
            if box_won[i//3][i%3]==0:
                for j in range(3):
                    for k in range(3):
                        if state[i//3][i%3][j][k]==0:
                            possible_indices.append([i,j,k]) 

    else:
        for l in range (3):
            for m in range(3):
                if state[box_to_play//3][box_to_play%3][l][m]==0:
                            possible_indices.append([box_to_play,l,m])     
    return possible_indices

def add_piece(state, move, player):
    #add a 1/2 on the state depends on who's playing
    state[move[0]//3][move[0]%3][move[1]][move[2]]=int(player)
    return state

def update_box_won(state):
    #create the matrix of the global board as if it is a local board
    temp_box_win = [[0 for _ in range(3)]for _ in range(3)]
    for b in range(9):
        box = state[b//3][b%3]
        temp_box_win[b//3][b%3] = check_box(box)
    return temp_box_win


def successors(state, player, last_move,box_won):
    #determine all the possible moves after a certain move
    succ = []
    moves_idx = []
    possible_indexes = possible_moves(state,last_move,box_won)
    for idx in possible_indexes:
        [x,y,z]=idx
        if state[x//3][x%3][y][z] ==0:
            new_state=[[[[i for i in state[l][k][j]]for j in range (len(state[l][k]))]for k in range (len(state[l]))]for l in range (len(state))]
            moves_idx.append(idx)
            succ.append(add_piece(new_state, idx, player))
    return zip(succ, moves_idx)

def opponent(p):
    #change the current player 
    return "2" if p == "1" else "1"


def evaluate_small_box(box_str, player):
    #evaluation function for the score in a local board
    global possible_goals
    score = 0
    three = Counter(player * 3)
    two = Counter(player * 2 +"0")
    one = Counter(player * 1 +"0" * 2)
    three_opponent = Counter(opponent(player) * 3)
    two_opponent = Counter(opponent(player) * 2 +"0")
    one_opponent = Counter(opponent(player) * 1 +"0" * 2)

    for idxs in possible_goals:
        (x, y, z) = idxs
        current = Counter([str(box_str[x[0]][x[1]]), str(box_str[y[0]][y[1]]), str(box_str[z[0]][z[1]])])

        if current == three:
            score += 100
        elif current == two:
            score += 10
        elif current == one:
            score += 1
        elif current == three_opponent:
            score -= 100
            return score
        elif current == two_opponent:
            score -= 10
        elif current == one_opponent:
            score -= 1

    return score


def evaluate(state, last_move, player,box_won):
    #evaluation function for the global board
    score = 0
    if check_box(box_won)==player:
        return inf
    elif check_box(box_won)==opponent(player):
        return -inf
    score += evaluate_small_box(box_won, player) * 200
    for b in range(9):
        box_str = state[b//3][b%3]
        score += evaluate_small_box(box_str, player)
    return score


def minimax(state, last_move_box,last_move_row,last_move_col, player, depth,box_won ):
    #function which predict the score for the chosen depth 
    last_move = (last_move_box,last_move_row,last_move_col)
    succ = list(successors(state, player, last_move,box_won))
    if not succ:
        return None
    best_move = (-inf, None)
    for s in succ:
        val = min_turn(s[0], s[1], opponent(player), depth-1,-inf, inf,box_won)
        if val > best_move[0]:
            best_move = (val, s)
    return best_move[1]


def min_turn(state, last_move, player, depth, alpha, beta,box_won):
    #function which minimaze the score of the player (player who you want to see win)
    if depth <= 0 or check_box(box_won) !=0:
        return evaluate(state, last_move, opponent(player),box_won)
    succ = successors(state, player, last_move,box_won)
    min_val = inf
    succ = list(successors(state, player, last_move,box_won))
    if not succ:
        return evaluate(state, last_move, opponent(player),box_won)
    for s in succ:
        val = max_turn(s[0], s[1], opponent(player), depth-1, alpha, beta,box_won)
        if val < min_val:
            min_val = val
        if min_val < beta:
            beta = min_val
        if alpha >= beta:
            break
    return min_val


def max_turn(state, last_move, player, depth, alpha, beta,box_won):
    #function which maximize the score of the player(player you want to see lose)
    if depth <= 0 or check_box(box_won) !=0 :
        return evaluate(state, last_move, player,box_won)
    max_val = -inf
    succ = list(successors(state, player, last_move,box_won))
    if not succ:
        return evaluate(state, last_move, player,box_won)
    for s in succ:
        val = min_turn(s[0], s[1], opponent(player), depth-1, alpha, beta,box_won)
        if val > max_val:
            max_val = val
        if max_val > alpha:
            alpha = max_val
        if alpha >= beta:
            break
    return max_val


