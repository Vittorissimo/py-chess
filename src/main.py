import numpy as np

def main():
    grid = np.matrix(9, 9)
    for col in range(9):
        for row in range(9):
            print("|__|" + grid[col][row] + "__|")

if __name__ == '__main__':
    main()