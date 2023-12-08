from typing import List


class Minigame:
    red_marbles = 0
    green_marbles = 0
    blue_marbles = 0

    def __str__(self):
        return "red: " + str(self.red_marbles) + " green: " + str(self.green_marbles) + \
            " blue: " + str(self.blue_marbles)

    def is_valid_for_part_1(self):
        return self.red_marbles <= 12 and self.green_marbles <= 13 and self.blue_marbles <= 14


class Game:
    id = None
    mini_games: None

    def is_valid_game(self):
        for mini_game in self.mini_games:
            if not mini_game.is_valid_for_part_1():
                return False
        return True

    def get_power(self):
        r = 1
        g = 1
        b = 1
        for mini_game in self.mini_games:
            if mini_game.red_marbles > r:
                r = mini_game.red_marbles
            if mini_game.green_marbles > g:
                g = mini_game.green_marbles
            if mini_game.blue_marbles > b:
                b = mini_game.blue_marbles
        return r * g * b


def game_parser(game_line: str):
    game = Game()
    split_line = game_line.split(": ")
    game.id = int(split_line[0].split(" ")[1])
    mini_games = split_line[1].split("; ")
    parsed_mini_games = []
    for mini_game in mini_games:
        parsed_mini_game = mini_game_parser(mini_game)
        parsed_mini_games.append(parsed_mini_game)
        game.mini_games = parsed_mini_games
    return game


def mini_game_parser(mini_game: str):
    minigame = Minigame()

    for marble_set in mini_game.split(', '):
        numOfMarbles = ''
        for i, v in enumerate(marble_set):
            if v.isdigit():
                numOfMarbles += v
                continue
            else:
                numOfMarbles = int(numOfMarbles)
                color = marble_set[i + 1]
                if color == 'r':
                    minigame.red_marbles = int(numOfMarbles)
                if color == 'g':
                    minigame.green_marbles = int(numOfMarbles)
                if color == 'b':
                    minigame.blue_marbles = int(numOfMarbles)
                break
    return minigame


def solve():
    file = open('day2-input.txt', 'r')
    lines = file.readlines()
    solution_part_1 = 0
    solution_part_2 = 0
    games = []
    for line in lines:
        game = game_parser(line)
        if game.is_valid_game():
            solution_part_1 += game.id

        solution_part_2 += game.get_power()
        games.append(game)

    print("Solution part 1: ", solution_part_1)
    print("Solution part 2: ", solution_part_2)


solve()
