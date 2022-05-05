import random
from colored import fore


class Maze:
    def __init__(self, size):
        self.characters = {
            'wall': 1,  # '#'
            'unvisited': '?',  # '?'
            'cell': 0,  # ' '
            'player': '*',  # '*'
            'bot': '@',  # '@'
            'path': '~'  # '~'
        }
        self.character_colors = {
            self.characters['wall']: fore.RED,
            self.characters['unvisited']: fore.WHITE,
            self.characters['cell']: fore.WHITE,
            self.characters['player']: fore.BLUE,
            self.characters['bot']: fore.YELLOW,
            self.characters['path']: fore.GREEN,
        }

        self.size = size
        self.player = [0, 0]
        self.maze = [[self.characters['unvisited'] for _ in range(size)] for _ in range(size)]

        self.vision = 4

    def surroundingCells(self, wall):
        return (self.maze[wall[0] - 1][wall[1]] == self.characters['cell']) + (
                    self.maze[wall[0] + 1][wall[1]] == self.characters['cell']) + (
                           self.maze[wall[0]][wall[1] - 1] == self.characters['cell']) + (
                           self.maze[wall[0]][wall[1] + 1] == self.characters['cell'])

    def generate(self):
        # Define variables
        global enter_x
        wall = self.characters['wall']
        cell = self.characters['cell']
        unvisited = self.characters['unvisited']
        walls = []
        # Pick starting point
        starting_height = random.randint(1, self.size - 2)
        starting_width = random.randint(1, self.size - 2)
        # Generate Starting Point
        self.maze[starting_height][starting_width] = cell
        self.maze[starting_height - 1][starting_width] = wall
        self.maze[starting_height + 1][starting_width] = wall
        self.maze[starting_height][starting_width - 1] = wall
        self.maze[starting_height][starting_width + 1] = wall
        walls.extend([[starting_height - 1, starting_width], [starting_height, starting_width - 1],
                      [starting_height, starting_width + 1], [starting_height + 1, starting_width]])

        # Repeat While Walls Have Values
        while len(walls) != 0:
            # Pick a random wall
            rand_wall_index = random.randint(0, len(walls) - 1)
            rand_wall = walls[rand_wall_index]
            # Check if it is a left wall
            if rand_wall[1] != 0:
                if self.maze[rand_wall[0]][rand_wall[1] - 1] == unvisited and self.maze[rand_wall[0]][rand_wall[1] + 1] == cell:
                    # Find the number of surrounding cells
                    s_cells = self.surroundingCells(rand_wall)

                    if s_cells < 2:
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = cell

                        # Mark the new walls
                        # Upper cell
                        if rand_wall[0] != 0:
                            if self.maze[rand_wall[0] - 1][rand_wall[1]] != cell:
                                self.maze[rand_wall[0] - 1][rand_wall[1]] = wall
                            if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                                walls.append([rand_wall[0] - 1, rand_wall[1]])

                        # Bottom cell
                        if rand_wall[0] != self.size - 1:
                            if self.maze[rand_wall[0] + 1][rand_wall[1]] != cell:
                                self.maze[rand_wall[0] + 1][rand_wall[1]] = wall
                            if [rand_wall[0] + 1, rand_wall[1]] not in walls:
                                walls.append([rand_wall[0] + 1, rand_wall[1]])

                        # Leftmost cell
                        if rand_wall[1] != 0:
                            if self.maze[rand_wall[0]][rand_wall[1] - 1] != cell:
                                self.maze[rand_wall[0]][rand_wall[1] - 1] = wall
                            if [rand_wall[0], rand_wall[1] - 1] not in walls:
                                walls.append([rand_wall[0], rand_wall[1] - 1])

                    # Delete wall
                    walls.pop(rand_wall_index)
                    continue

            # Check if it is an upper wall
            if rand_wall[0] != 0:
                if self.maze[rand_wall[0] - 1][rand_wall[1]] == unvisited and self.maze[rand_wall[0] + 1][rand_wall[1]] == cell:

                    s_cells = self.surroundingCells(rand_wall)
                    if s_cells < 2:
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = cell

                        # Mark the new walls
                        # Upper cell
                        if rand_wall[0] != 0:
                            if self.maze[rand_wall[0] - 1][rand_wall[1]] != cell:
                                self.maze[rand_wall[0] - 1][rand_wall[1]] = wall
                            if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                                walls.append([rand_wall[0] - 1, rand_wall[1]])

                        # Leftmost cell
                        if rand_wall[1] != 0:
                            if self.maze[rand_wall[0]][rand_wall[1] - 1] != cell:
                                self.maze[rand_wall[0]][rand_wall[1] - 1] = wall
                            if [rand_wall[0], rand_wall[1] - 1] not in walls:
                                walls.append([rand_wall[0], rand_wall[1] - 1])

                        # Rightmost cell
                        if rand_wall[1] != self.size - 1:
                            if self.maze[rand_wall[0]][rand_wall[1] + 1] != cell:
                                self.maze[rand_wall[0]][rand_wall[1] + 1] = wall
                            if [rand_wall[0], rand_wall[1] + 1] not in walls:
                                walls.append([rand_wall[0], rand_wall[1] + 1])

                    # Delete wall
                    walls.pop(rand_wall_index)
                    continue

            # Check the bottom wall
            if rand_wall[0] != self.size - 1:
                if self.maze[rand_wall[0] + 1][rand_wall[1]] == unvisited and self.maze[rand_wall[0] - 1][rand_wall[1]] == cell:

                    s_cells = self.surroundingCells(rand_wall)
                    if s_cells < 2:
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = cell

                        # Mark the new walls
                        if rand_wall[0] != self.size - 1:
                            if self.maze[rand_wall[0] + 1][rand_wall[1]] != cell:
                                self.maze[rand_wall[0] + 1][rand_wall[1]] = wall
                            if [rand_wall[0] + 1, rand_wall[1]] not in walls:
                                walls.append([rand_wall[0] + 1, rand_wall[1]])
                        if rand_wall[1] != 0:
                            if self.maze[rand_wall[0]][rand_wall[1] - 1] != cell:
                                self.maze[rand_wall[0]][rand_wall[1] - 1] = wall
                            if [rand_wall[0], rand_wall[1] - 1] not in walls:
                                walls.append([rand_wall[0], rand_wall[1] - 1])
                        if rand_wall[1] != self.size - 1:
                            if self.maze[rand_wall[0]][rand_wall[1] + 1] != cell:
                                self.maze[rand_wall[0]][rand_wall[1] + 1] = wall
                            if [rand_wall[0], rand_wall[1] + 1] not in walls:
                                walls.append([rand_wall[0], rand_wall[1] + 1])

                    # Delete wall
                    walls.pop(rand_wall_index)
                    continue

            # Check the right wall
            if rand_wall[1] != self.size - 1:
                if self.maze[rand_wall[0]][rand_wall[1] + 1] == unvisited and self.maze[rand_wall[0]][rand_wall[1] - 1] == cell:

                    s_cells = self.surroundingCells(rand_wall)
                    if s_cells < 2:
                        # Denote the new path
                        self.maze[rand_wall[0]][rand_wall[1]] = cell

                        # Mark the new walls
                        if rand_wall[1] != self.size - 1:
                            if self.maze[rand_wall[0]][rand_wall[1] + 1] != cell:
                                self.maze[rand_wall[0]][rand_wall[1] + 1] = wall
                            if [rand_wall[0], rand_wall[1] + 1] not in walls:
                                walls.append([rand_wall[0], rand_wall[1] + 1])
                        if rand_wall[0] != self.size - 1:
                            if self.maze[rand_wall[0] + 1][rand_wall[1]] != cell:
                                self.maze[rand_wall[0] + 1][rand_wall[1]] = wall
                            if [rand_wall[0] + 1, rand_wall[1]] not in walls:
                                walls.append([rand_wall[0] + 1, rand_wall[1]])
                        if rand_wall[0] != 0:
                            if self.maze[rand_wall[0] - 1][rand_wall[1]] != cell:
                                self.maze[rand_wall[0] - 1][rand_wall[1]] = wall
                            if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                                walls.append([rand_wall[0] - 1, rand_wall[1]])

                    # Delete wall
                    walls.pop(rand_wall_index)
                    continue

            # Delete the wall from the list anyway
            walls.pop(rand_wall_index)

        # Mark Unvisited As Walls
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.maze[i][j] == unvisited:
                    self.maze[i][j] = wall

        enter_x, exit_x = 0, 0

        for i in range(0, self.size):
            if self.maze[1][i] == cell:
                self.maze[0][i] = cell
                enter_x = (0, i)
                break
        for i in range(self.size - 1, 0, -1):
            if self.maze[self.size - 2][i] == cell:
                self.maze[self.size - 1][i] = cell
                exit_x = (self.size - 1, i)
                break
        return enter_x, exit_x

    def render(self):
        display = ''
        for i in range(self.size):
            for j in range(self.size):
                element = self.maze[i][j]
                display += self.character_colors[element] + str(element) + ' '
            display += '\n'
        return display

    def renderpb(self, player, bot, blindness=False):
        if player[0] < 0 or self.size <= player[0] or player[1] < 0 or self.size <= player[1]:
            return None
        if bot[0] < 0 or self.size <= bot[0] or bot[1] < 0 or self.size <= bot[1]:
            return None

        display = ''

        if blindness:
            x_start = [player[0] - self.vision, 0][0 > player[0] - self.vision]
            x_end = [player[0] + self.vision, self.size - 1][self.size <= player[0] + self.vision]
            y_start = [player[1] - self.vision, 0][0 > player[1] - self.vision]
            y_end = [player[1] + self.vision, self.size - 1][self.size <= player[1] + self.vision]

            for i in range(x_start, x_end + 1):
                for j in range(y_start, y_end + 1):
                    if player[0] == i and player[1] == j:
                        display += f"{self.character_colors[self.characters['player']]}{self.characters['player']} "
                    elif bot[0] == i and bot[1] == j:
                        display += f"{self.character_colors[self.characters['bot']]}{self.characters['bot']} "
                    else:
                        element = self.maze[i][j]
                        display += self.character_colors[element] + str(element) + ' '
                display += '\n'
        else:
            for i in range(self.size):
                for j in range(self.size):
                    if player[0] == i and player[1] == j:
                        display += f"{self.character_colors[self.characters['player']]}{self.characters['player']} "
                    elif bot[0] == i and bot[1] == j:
                        display += f"{self.character_colors[self.characters['bot']]}{self.characters['bot']} "
                    else:
                        element = self.maze[i][j]
                        display += f"{self.character_colors[element]}{element} "
                display += '\n'
        return display

    def render_player_bot(self, player, bot, blindness=False):
        self.renderpb(player, bot, blindness)

    def cell(self, x, y):
        return self.maze[x][y]

    def get_maze(self):
        return self.maze

    def bot_move(self, bot, player):
        # This 'AI' isn't the best, but I'm too lazy
        #      to come up with something good

        # Check in wich direction bot should move
        if bot[0] <= player[0] and bot[1] <= player[1]:
            # Move Down Right
            if self.cell(bot[0] + 1, bot[1]) in [' ', '*'] and self.cell(bot[0], bot[1] + 1) in [' ', '*']:
                bot[random.randint(0, 1)] += 1
            elif self.cell(bot[0] + 1, bot[1]) in [' ', '*']:
                bot[0] += 1
            elif self.cell(bot[0], bot[1] + 1) in [' ', '*']:
                bot[1] += 1
            else:
                if self.cell(bot[0] - 1, bot[1]) in [' ', '*'] and self.cell(bot[0], bot[1] - 1) in [' ', '*']:
                    bot[random.randint(0, 1)] -= 1
                elif self.cell(bot[0] - 1, bot[1]) in [' ', '*']:
                    bot[0] -= 1
                else:
                    bot[1] -= 1
        elif bot[0] < player[0] and bot[1] > player[1]:
            # Move Down Left
            if self.cell(bot[0] + 1, bot[1]) in [' ', '*'] and self.cell(bot[0], bot[1] - 1) in [' ', '*']:
                if random.randint(0, 1) == 0:
                    bot[0] += 1
                else:
                    bot[1] -= 1
            elif self.cell(bot[0] + 1, bot[1]) in [' ', '*']:
                bot[0] += 1
            elif self.cell(bot[0], bot[1] - 1) in [' ', '*']:
                bot[1] -= 1
            else:
                if self.cell(bot[0] - 1, bot[1]) in [' ', '*'] and self.cell(bot[0], bot[1] + 1) in [' ', '*']:
                    if random.randint(0, 1) == 0:
                        bot[0] -= 1
                    else:
                        bot[1] += 1
                elif self.cell(bot[0] - 1, bot[1]) in [' ', '*']:
                    bot[0] -= 1
                else:
                    bot[1] += 1
        elif bot[0] > player[0] and bot[1] <= player[1]:
            # Move Up Right
            if self.cell(bot[0] - 1, bot[1]) in [' ', '*'] and self.cell(bot[0], bot[1] + 1) in [' ', '*']:
                if random.randint(0, 1) == 0:
                    bot[0] -= 1
                else:
                    bot[1] += 1
            elif self.cell(bot[0] - 1, bot[1]) in [' ', '*']:
                bot[0] -= 1
            elif self.cell(bot[0], bot[1] + 1) in [' ', '*']:
                bot[1] += 1
            else:
                if self.cell(bot[0] + 1, bot[1]) in [' ', '*'] and self.cell(bot[0], bot[1] - 1) in [' ', '*']:
                    if random.randint(0, 1) == 0:
                        bot[0] += 1
                    else:
                        bot[1] -= 1
                elif self.cell(bot[0] - 1, bot[1]) in [' ', '*']:
                    bot[0] += 1
                else:
                    bot[1] -= 1
        elif bot[0] > player[0] and bot[1] > player[1]:
            # Move Up Left
            if self.cell(bot[0] - 1, bot[1]) in [' ', '*'] and self.cell(bot[0], bot[1] - 1) in [' ', '*']:
                bot[random.randint(0, 1)] -= 1
            elif self.cell(bot[0] - 1, bot[1]) in [' ', '*']:
                bot[0] -= 1
            elif self.cell(bot[0], bot[1] - 1) in [' ', '*']:
                bot[1] -= 1
            else:
                if self.cell(bot[0] + 1, bot[1]) in [' ', '*'] and self.cell(bot[0], bot[1] + 1) in [' ', '*']:
                    bot[random.randint(0, 1)] += 1
                elif self.cell(bot[0] + 1, bot[1]) in [' ', '*']:
                    bot[0] += 1
                else:
                    bot[1] += 1
        else:
            pass
        return bot

    def render_path(self, path):
        display = ''
        for i in range(self.size):
            for j in range(self.size):
                element = self.maze[i][j]
                if (i, j) in path:
                    display += f"{self.character_colors[self.characters['path']]}{self.characters['path']} "
                else:
                    display += f"{self.character_colors[element]}{element} "
            display += f"\n{fore.WHITE}"
        return display
