def is_valid_move(global_board, local_boards, global_row, global_col, local_row, local_col, prev_local_row, prev_local_col):
    #check all the move we can do 
    if global_board[global_row][global_col] != 0:
        return False
    if local_boards[global_row][global_col][local_row][local_col] != 0:
        return False

    if prev_local_row is not None and prev_local_col is not None:
        if (global_row, global_col) != (prev_local_row, prev_local_col):
            return False
    return True

def is_valid_move_2(global_board, local_boards, global_row, global_col, local_row, local_col):
    #same thing
    if global_board[global_row][global_col] != 0:
        return False
    if local_boards[global_row][global_col][local_row][local_col] != 0:
        return False
    if local_board_won(local_boards[global_row][global_col]) or local_board_full(local_boards[global_row][global_col]):
        return False
    return True

def local_board_won(local_board):
    for i in range(3):
        if local_board[i][0] == local_board[i][1] == local_board[i][2] != 0 or \
           local_board[0][i] == local_board[1][i] == local_board[2][i] != 0:
            return True
    if local_board[0][0] == local_board[1][1] == local_board[2][2] != 0 or \
       local_board[0][2] == local_board[1][1] == local_board[2][0] != 0:
        return True
    return False

def local_board_full(local_board):
    for row in local_board:
        for cell in row:
            if cell == 0:
                return False
    return True

def check_local_board_win(local_board, current_player):
    for i in range(3):
        if local_board[i][0] == local_board[i][1] == local_board[i][2] == current_player or \
           local_board[0][i] == local_board[1][i] == local_board[2][i] == current_player:
            return True
    if local_board[0][0] == local_board[1][1] == local_board[2][2] == current_player or \
       local_board[0][2] == local_board[1][1] == local_board[2][0] == current_player:
        return True
    return False

def check_global_board_win(global_board, current_player):
    for i in range(3):
        if global_board[i][0] == global_board[i][1] == global_board[i][2] == current_player or \
           global_board[0][i] == global_board[1][i] == global_board[2][i] == current_player:
            return True
    if global_board[0][0] == global_board[1][1] == global_board[2][2] == current_player or \
       global_board[0][2] == global_board[1][1] == global_board[2][0] == current_player:
        return True
    return False

def check_global_board_draw(global_board, local_boards):
    for i in range(3):
        for j in range(3):
            if global_board[i][j] == 0 and not (local_board_full(local_boards[i][j]) or local_board_won(local_boards[i][j])):
                return False
    return True

def evaluate_position(global_board, local_boards, current_player,depth):

    all_local_boards_full = all(local_board_full(local_board) or local_board_won(local_board) for row in local_boards for local_board in row)

    # Check for a win in the global board
    if check_global_board_win(global_board,1):
        return float('inf')
    if check_global_board_win(global_board,2):
        return -float('inf')
    # Check for a draw in the global board
    elif all_local_boards_full:
        return 0

    # Evaluate the position based on local board wins and progress
    score = 0
    for i in range(3):
        for j in range(3):
            local_board = local_boards[i][j]
            score += evaluate_local_board(local_board, 1,depth)
    score += check_two_aligned_local(local_board, 1,depth)
    score += check_two_aligned_global(global_board, 1,depth)

    for i in range(3):
        for j in range(3):
            local_board = local_boards[i][j]
            score -= evaluate_local_board(local_board, 2,depth)
    score -= check_two_aligned_local(local_board, 2,depth)
    score -= check_two_aligned_global(global_board, 2,depth)
    return score

def evaluate_local_board(local_board, current_player,depth):
    # Check for a win in the local board
    if check_local_board_win(local_board, current_player):
        return 200*(depth+1)
    # Check for progress towards a win
    else:
        return 0

def check_two_aligned_local(local_board, current_player,depth):
    #check if there are two alligned cell for one player
    count = 0
    #row
    for row in local_board:
        if row.count(current_player) == 2 and row.count(0) == 1:
            count += 30*(depth+1)

    # column
    for col in range(3):
        column = [local_board[row][col] for row in range(3)]
        if column.count(current_player) == 2 and column.count(0) == 1:
            count += 30*(depth+1)

    #diagonales
    diagonal1 = [local_board[i][i] for i in range(3)]
    diagonal2 = [local_board[i][2 - i] for i in range(3)]
    if diagonal1.count(current_player) == 2 and diagonal1.count(0) == 1:
        count += 30*(depth+1)

    if diagonal2.count(current_player) == 2 and diagonal2.count(0) == 1:
        count += 30*(depth+1)

    return count

def check_two_aligned_global(global_board, current_player,depth):
    #verify if there are two aligned local boards won
    count = 0
    # row
    for row in global_board:
        if row.count(current_player) == 2 and row.count(0) == 1:
            count += 70*(depth+1)

    # column
    for col in range(3):
        column = [global_board[row][col] for row in range(3)]
        if column.count(current_player) == 2 and column.count(0) == 1:
            count += 70*(depth+1)

    # diagonale
    diagonal1 = [global_board[i][i] for i in range(3)]
    diagonal2 = [global_board[i][2 - i] for i in range(3)]
    if diagonal1.count(current_player) == 2 and diagonal1.count(0) == 1:
        count += 70*(depth+1)
    if diagonal2.count(current_player) == 2 and diagonal2.count(0) == 1:
        count += 70*(depth+1)

    return count

def alpha_beta_pruning(global_board, local_boards, depth, alpha, beta, maximizing_player, prev_local_row, prev_local_col,dfixe):
    #function which compute the score and find the best move
    valid_moves = [(i, j, x, y) for i in range(3) for j in range(3) for x in range(3) for y in range(3)
                   if is_valid_move(global_board, local_boards, i, j, x, y, prev_local_row, prev_local_col)]

    if not valid_moves:
        valid_moves = [(i, j, x, y) for i in range(3) for j in range(3) for x in range(3) for y in range(3)
                       if is_valid_move_2(global_board, local_boards, i, j, x, y)]

    if depth == 0 or check_global_board_win(global_board, 1) or check_global_board_win(global_board, 2) or check_global_board_draw(global_board, local_boards) or not valid_moves:
        return evaluate_position(global_board, local_boards, 1 if maximizing_player else 2,depth), (-1, -1, -1, -1)

    if maximizing_player:
        max_eval = (-float('inf'), (-1, -1, -1, -1))
        for move in valid_moves:
            new_global_board = [[global_board[i][j] for i in range(3)] for j in range(3)]
            new_local_boards = [[[[i for i in local_boards[l][k][j]]for j in range (len(local_boards[l][k]))]for k in range (len(local_boards[l]))]for l in range (len(local_boards))]
            global_row, global_col, local_row, local_col = move
            new_local_boards[move[0]][move[1]][move[2]][move[3]] = 1
            if check_local_board_win(new_local_boards[global_row][global_col], 1):
                new_global_board[global_row][global_col] = 1
            
            if check_global_board_win(new_global_board, 1) and depth==dfixe:
                print("rentré dedans")
                eval=float('inf')
                return (eval,move)
            eval = alpha_beta_pruning(new_global_board, new_local_boards, depth - 1, alpha, beta, False,local_row, local_col,dfixe)[0]
            max_eval = max(max_eval, (eval, move), key=lambda x: x[0])
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval

    else:
        min_eval = (float('inf'), (-1, -1, -1, -1))
        for move in valid_moves:
            new_global_board = [[global_board[i][j] for i in range(3)] for j in range(3)]
            new_local_boards = [[[[i for i in local_boards[l][k][j]]for j in range (len(local_boards[l][k]))]for k in range (len(local_boards[l]))]for l in range (len(local_boards))]

            global_row, global_col, local_row, local_col = move
            new_local_boards[move[0]][move[1]][move[2]][move[3]] = 2
            if check_local_board_win(new_local_boards[global_row][global_col], 2):
                global_board[global_row][global_col] = 2
            if check_global_board_win(new_global_board, 2):
                eval=-float('inf')
                return(eval,move)
            eval = alpha_beta_pruning(new_global_board, new_local_boards, depth - 1, alpha, beta, True,
                                       local_row, local_col,dfixe)[0]
            min_eval = min(min_eval, (eval, move), key=lambda x: x[0])
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
