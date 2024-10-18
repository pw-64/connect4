from main import Main

def new_grid():
    return [["" for _ in range(0, 10)] for _ in range(0, 10)]

def check_for_win(grid):
    main = Main(grid)
    assert main.check_for_win(counter, (counter == "O") + 1)

if __name__ == "__main__":
    for counter in ["X", "O"]:

        """
        x x x x
        """
        print(f"\n{counter} straight horizontal:")
        grid = new_grid()
        grid[0][0] = grid[0][1] = grid[0][2] = grid[0][3] = counter
        check_for_win(grid)


        """
        x
        x
        x
        x
        """
        print(f"\n{counter} straight vertical:")
        grid = new_grid()
        grid[0][0] = grid[1][0] = grid[2][0] = grid[3][0] = counter
        check_for_win(grid)


        """
        x
          x
            x
              x
        """
        print(f"\n{counter} diagonal south east:")
        grid = new_grid()
        grid[0][0] = grid[1][1] = grid[2][2] = grid[3][3] = counter
        check_for_win(grid)


        """
              x
            x
          x
        x
        """
        print(f"\n{counter} diagonal north east:")
        grid = new_grid()
        grid[0][3] = grid[1][2] = grid[2][1] = grid[3][0] = counter
        check_for_win(grid)

        print()
    
    print("All winner checks were successful \n")