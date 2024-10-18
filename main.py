# grid formatting
divider_row = f"|{"-" * 59}|"
corner_row = f"+{"-" * 59}+"
spacer_row = f"|{"     |" * 10}"

class Main:
    def __init__(self, grid=None):
        # if not given, create a 10 x 10 grid of empty strings (10 per sublist, 10 sublists = 100 strings)
        self.grid = grid or [["" for _ in range(0, 10)] for _ in range(0, 10)]

        # grid[0][0] is top left
        # grid[9][9] is bottom right

    def display_canvas(self):
        print("", corner_row, sep="\n")
        for row in range(9):
            print(spacer_row, "".join([f"|{self.grid[row][slot]:^5}" for slot in range(10)]) + "|", spacer_row, divider_row, sep="\n")
        print(spacer_row, "".join([f"|{self.grid[9][slot]:^5}" for slot in range(10)]) + "|", spacer_row, corner_row, "", sep="\n")

    def place_counter(self, column, counter):
        column -= 1 # convert user-understandable number into the list index
        # put the counter into the unused slot closest to the bottom of the column
        for row in self.grid[::-1]:
            if row[column] == "":
                row[column] = counter
                return

    def check_for_win(self, counter, player_number):
        won = False

        # check for straight line in each row
        for row in self.grid:
            for slot in range(7):
                if ((row[slot] == counter) and
                    (row[slot + 1] == counter) and
                    (row[slot + 2] == counter) and
                    (row[slot + 3] == counter)
                    ):
                    won = True

        if not won:
            # check for straight line in each column
            for row in range(3, 10):
                for slot in range(10):
                    if ((self.grid[row][slot] == counter) and
                        (self.grid[row - 1][slot] == counter) and
                        (self.grid[row - 2][slot] == counter) and
                        (self.grid[row - 3][slot] == counter)
                        ):
                        won = True

        if not won:
            # check for diagonals north-east / south-west
            for row in range(3, 10):
                for slot in range(8):
                    if ((self.grid[row][slot] == counter) and
                        (self.grid[row - 1][slot + 1] == counter) and
                        (self.grid[row - 2][slot + 2] == counter) and
                        (self.grid[row - 3][slot + 3] == counter)
                        ):
                        won = True

        if not won:
            # check for diagonals south-east / north-west
            for row in range(7):
                for slot in range(8):
                    if ((self.grid[row][slot] == counter) and
                        (self.grid[row + 1][slot + 1] == counter) and
                        (self.grid[row + 2][slot + 2] == counter) and
                        (self.grid[row + 3][slot + 3] == counter)
                        ):
                        won = True

        if won:
            print(f"Winner is: Player {player_number}!")

        return won

    # end the game if there are no more spaces to drop a counter
    def check_if_slots_left(self):
        slots_taken = 0
        for row in self.grid:
            for slot in row:
                if slot != "":
                    slots_taken += 1

        if slots_taken == 100:
            print("Game Over - Out of slots")

        return slots_taken == 100

    # ask player which column to "drop" their counter into out of the available ones
    def ask_for_column(self, player_number, available_columns):
        while True:
            try:
                column = int(input(f"Player {player_number} choose a column ({",".join([str(c) for c in available_columns])}): "))
            except ValueError:
                print(f"Invalid input - Must be one of these: {available_columns}")
                continue  # value is already invalid so skip the next if otherwise it will always trigger the second invalid message
            if column not in available_columns:
                print(f"Invalid input - Must be one of these: {available_columns}")
            else: break
        return column

    # return a list of columns with slots remaining to be filled
    def get_available_columns(self):
        available_columns = []
        for i in range(10):
            if self.grid[0][i] == "":
                available_columns.append(i + 1)
        return available_columns

    def player_turn(self, player_number, player_symbol):
        self.place_counter(
            self.ask_for_column(
                player_number,
                self.get_available_columns()
            ),
            player_symbol
        )
        self.display_canvas()
        return self.check_for_win(player_symbol, player_number) or self.check_if_slots_left()
    
    def run(self):
        try:
            while True:
                if (self.player_turn(1, "X")
                    or self.player_turn(2, "O")
                    # can add more players - unique number and symbol
                    # or self.player_turn(3, "A")
                    # or self.player_turn(4, "B")
                    # ...
                    ):
                    return
        except KeyboardInterrupt:
            quit()

if __name__ == "__main__":
    Main().run()