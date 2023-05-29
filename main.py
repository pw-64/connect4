# create a 10 x 10 grid of empty strings (10 per sublist, 10 sublists = 100 strings)
canvas = []
for i in range(0, 10):
    canvas.append([])
    for _ in range(0, 10): canvas[i].append('')

row1 = canvas[9]; row2 = canvas[8]; row3 = canvas[7]; row4 = canvas[6]; row5 = canvas[5]; row6 = canvas[4]; row7 = canvas[3]; row8 = canvas[2]; row9 = canvas[1]; row10 = canvas[0]
rows = [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10]

# print a nice-looking grid to the shell (includes outlining border around the edge)
divider_row = f'\t|{"-" * 159}|'; corner_row = f'\t+{"-" * 159}+'; spacer_row = f'\t|' + '\t\t|' * 10
def display_canvas():
    print('\n', corner_row)
    for i in [9, 8, 7, 6, 5, 4, 3, 2, 1]: print(spacer_row, f'\t|\t{rows[i][0]}\t|\t{rows[i][1]}\t|\t{rows[i][2]}\t|\t{rows[i][3]}\t|\t{rows[i][4]}\t|\t{rows[i][5]}\t|\t{rows[i][6]}\t|\t{rows[i][7]}\t|\t{rows[i][8]}\t|\t{rows[i][9]}\t|', spacer_row, divider_row, sep='\n')
    print(spacer_row, f'\t|\t{rows[0][0]}\t|\t{rows[0][1]}\t|\t{rows[0][2]}\t|\t{rows[0][3]}\t|\t{rows[0][4]}\t|\t{rows[0][5]}\t|\t{rows[0][6]}\t|\t{rows[0][7]}\t|\t{rows[0][8]}\t|\t{rows[0][9]}\t|', spacer_row, corner_row, sep='\n')

def place_counter(column, counter):
    column -= 1 # convert user-understandable number into the list index
    # put the counter into the unused slot closest to the bottom of the column
    for row in rows:
        if row[column] == '': row[column] = counter; break

def check_for_win(counter, player_number):
    winner = None

    # check for straight line in each row
    for row in rows:
        for i in range(0, 7):
            if (row[i] == counter) and (row[i+1] == counter) and (row[i+2] == counter) and (row[i+3] == counter): winner = f'Player {player_number}'

    # check for straight line in each column
    for index in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if (row1[index] == counter) and (row2[index] == counter) and (row3[index] == counter) and (row4[index] == counter): winner = f'Player {player_number}'
        if (row2[index] == counter) and (row3[index] == counter) and (row4[index] == counter) and (row5[index] == counter): winner = f'Player {player_number}'
        if (row3[index] == counter) and (row4[index] == counter) and (row5[index] == counter) and (row6[index] == counter): winner = f'Player {player_number}'
        if (row4[index] == counter) and (row5[index] == counter) and (row6[index] == counter) and (row7[index] == counter): winner = f'Player {player_number}'
        if (row5[index] == counter) and (row6[index] == counter) and (row7[index] == counter) and (row8[index] == counter): winner = f'Player {player_number}'
        if (row6[index] == counter) and (row7[index] == counter) and (row8[index] == counter) and (row9[index] == counter): winner = f'Player {player_number}'
        if (row7[index] == counter) and (row8[index] == counter) and (row9[index] == counter) and (row10[index] == counter): winner = f'Player {player_number}'

    # check for diagonals (bottom left -> top right or vice versa)
    for row_number in [1, 2, 3, 4, 5, 6]:
        for index in [0, 1, 2, 3, 4, 5, 6, 7]:
            exec_output = {}; exec(f'\
if (row{row_number}[{index}] == "{counter}") and\
(row{row_number + 1}[{index+1}] == "{counter}") and\
(row{row_number + 2}[{index+2}] == "{counter}") and\
(row{row_number + 3}[{index+3}] == "{counter}"): found = True', globals(), exec_output)
            if exec_output.get('found'): winner = f'Player {player_number}'

    # check for diagonals (top left -> bottom right or vice versa)
    for row_number in [9, 8, 7, 6, 5, 4]:
        for index in [0, 1, 2, 3, 4, 5, 6, 7]:
            exec_output = {}; exec(f'\
if (row{row_number}[{index}] == "{counter}") and\
(row{row_number - 1}[{index+1}] == "{counter}") and\
(row{row_number - 2}[{index+2}] == "{counter}") and\
(row{row_number - 3}[{index+3}] == "{counter}"): found = True', globals(), exec_output)
            if exec_output.get('found'): winner = f'Player {player_number}'
    
    # quit game and display winner if there is one
    if winner is not None: quit(f'Winner is: {winner}!')

# end the game if there are no more spaces to drop a counter and if noone has won already
def check_if_slots_left():
    slots_taken = 0
    for row in rows:
        for slot in row:
            if slot != '': slots_taken += 1
    if slots_taken == 100: quit('Game Over - Out of slots')

# ask player which column to "drop" their counter into out of the available ones
def ask_for_column(player_number, available_columns):
    while True:
        try: column = int(input(f'Player {player_number} - Column ({available_columns}): '))
        except: print(f'Invalid input - Must be one of these: {available_columns}'); continue                    # catches an error if a non-int is inputted
        if column not in available_columns: print(f'Invalid input - Must be one of these: {available_columns}')  # if the input is an int but it isnt an available option
        else: break
    return column

# return a list of columns with slots remaining to be filled
def get_available_columns():
    available_columns = []
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if row10[i] != '': pass
        else: available_columns.append(i + 1)
    return available_columns

def main(player_number, player_symbol):
    place_counter(ask_for_column(player_number, get_available_columns()), player_symbol)
    display_canvas()
    check_for_win(player_symbol, player_number)
    check_if_slots_left()

while True:
    main(1, 'X') # player 1
    main(2, 'O') # player 2