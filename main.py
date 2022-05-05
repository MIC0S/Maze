# import random
import bot as bt
from colored import fore
import maze
import os


def cls():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def main():
    size = 20
    mz = maze.Maze(size)
    mz.generate()
    player, bot, moves = [1, 1], [0, 1], 0
    astar = bt.AStar()
    while True:
        cls()
        print(mz.renderpb(player, bot, True))
        inp = input(f"{fore.WHITE}[W] [A] [S] [D]\n").lower()
        if inp == 'w' and mz.cell(player[0] - 1, player[1]) == 0:
            player[0] -= 1
        elif inp == 'a' and mz.cell(player[0], player[1] - 1) == 0:
            player[1] -= 1
        elif inp == 's' and mz.cell(player[0] + 1, player[1]) == 0:
            player[0] += 1
        elif inp == 'd' and mz.cell(player[0], player[1] + 1) == 0:
            player[1] += 1
        elif inp == 'q':
            print(mz.render())
        moves += 1
        if moves > 3:
            astar.path_render(mz.get_maze(), tuple(bot), tuple(player))
            bot = list(astar.move(mz.get_maze(), tuple(bot), tuple(player)))
        if player[0] == bot[0] and player[1] == bot[1]:
            win = False
            break
        if player[0] == size - 1 and player[1] == size - 2:
            win = True
            break
    cls()
    if win:
        print(f"{mz.renderpb(player, bot, True)}\n{fore.BLUE}VICTORY!")
    else:
        print(f"{mz.renderpb(player, bot, True)}\n{fore.MAGENTA}LOOSE!")


if __name__ == '__main__':
    main()