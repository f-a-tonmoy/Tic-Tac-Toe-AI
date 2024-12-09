from random import randint, choice
from colorama import Fore as clr
from time import sleep

N = 4


class Board:
    def __init__(self):
        self.states = [['.' for _ in range(N)] for _ in range(N)]
        self.coords = [(j, i) for j in range(N) for i in range(N)]

        self.val = (4 * N) + (N - 1) if N > 4 else 19
        print('=' * self.val)
        print(f'{"TIC TAC TOE": ^{self.val}}')
        print('=' * self.val)
        print(f'{"1. EASY | 2. HARD": ^{self.val}}')
        print('=' * self.val)

    def draw_board(self, move_coords, win_coords):
        num = 1
        for i in range(N):
            print('', end=' ' if N > 3 else '   ')
            for j in range(N):
                val = self.states[i][j]
                if win_coords and (i, j) in win_coords:
                    print(f'{clr.CYAN} {val:2}', end='')
                elif (i, j) == move_coords:
                    print(f'{clr.YELLOW} {val:2}', end='')
                else:
                    if val == 'O':
                        print(f'{clr.RED} {val:2}', end='')
                    elif val == 'X':
                        print(f'{clr.GREEN} {val:2}', end='')
                    else:
                        print(f'{clr.MAGENTA}{num:2} ', end='')

                num += 1
                print(f'{clr.RESET}{"|" if j < N - 1 else ""}', end=' ')

            print(f'\n{"" if N > 3 else "  "}{"|".join(["----"] * N)}' if i < N - 1 else '')
        print()

    def evaluation(self, x, y):
        self.states[x][y] = 'O'
        x_available, o_available = 0, 0

        for i in range(N):
            x_available += 1 if 'O' not in self.states[i] else 0
            o_available += 1 if 'X' not in self.states[i] else 0

            col_vals = [self.states[j][i] for j in range(N)]
            x_available += 1 if 'O' not in col_vals else 0
            o_available += 1 if 'X' not in col_vals else 0

        diags = [self.states[i][i] for i in range(N)]
        x_available += 1 if 'O' not in diags else 0
        o_available += 1 if 'X' not in diags else 0

        anti_diags = [self.states[i][N - 1 - i] for i in range(N)]
        x_available += 1 if 'O' not in anti_diags else 0
        o_available += 1 if 'X' not in anti_diags else 0

        self.states[x][y] = '.'
        return x_available - o_available

    def possible_win(self):
        for i in range(N):
            row = self.states[i]
            if '.' in row and row.count('X') == N - 1:
                return i, row.index('.')

            col = [self.states[j][i] for j in range(N)]
            if '.' in col and col.count('X') == N - 1:
                return col.index('.'), i

        diag = [self.states[i][i] for i in range(N)]
        if '.' in diag and diag.count('X') == N - 1:
            i = diag.index('.')
            return i, i

        anti_diag = [self.states[i][N - 1 - i] for i in range(N)]
        if '.' in anti_diag and anti_diag.count('X') == N - 1:
            i = anti_diag.index('.')
            return i, N - 1 - i

        return None

    def check_winner(self):
        for i in range(N):
            winner = self.all_marked(self.states[i])
            if winner: return winner, [(i, j) for j in range(N)]

            winner = self.all_marked([self.states[j][i] for j in range(N)])
            if winner: return winner, [(j, i) for j in range(N)]

        winner = self.all_marked([self.states[i][i] for i in range(N)])
        if winner: return winner, [(i, i) for i in range(N)]

        winner = self.all_marked([self.states[i][N - 1 - i] for i in range(N)])
        if winner: return winner, [(i, N - 1 - i) for i in range(N)]

        empty_cell = any('.' in row for row in self.states)

        return (None, None) if empty_cell else ('.', None)

    @staticmethod
    def all_marked(marked):
        if marked == ['X'] * N: return 'X'
        if marked == ['O'] * N: return 'O'

        return None


class AlphaBeta(Board):
    def __init__(self):
        super().__init__()
        self.utilities = {'O': -1, '.': 0, 'X': 1}

    def max_ab(self, alpha, beta, x=None, y=None):
        winner, _ = self.check_winner()
        if winner: return self.utilities[winner], '', ''

        for i in range(N):
            for j in range(N):
                if self.states[i][j] != '.': continue

                self.states[i][j] = 'X'
                val, _, _ = self.min_ab(alpha, beta)
                self.states[i][j] = '.'

                if val > alpha: alpha, x, y = val, i, j
                if alpha >= beta: return alpha, x, y

        return alpha, x, y

    def min_ab(self, alpha, beta, x=None, y=None):
        winner, _ = self.check_winner()
        if winner: return self.utilities[winner], '', ''

        for i in range(N):
            for j in range(N):
                if self.states[i][j] != '.': continue

                self.states[i][j] = 'O'
                val, _, _ = self.max_ab(alpha, beta)
                self.states[i][j] = '.'

                if val < beta: beta, x, y = val, i, j
                if alpha >= beta: return beta, x, y

        return beta, x, y


class Game(AlphaBeta):
    def __init__(self):
        super().__init__()
        self.steps = 0
        self.is_easy = False
        self.player_turn = 'X'

        self.end_msg = {
            'X': 'YOU WON! 😀',
            'O': 'AI WON! 🤖',
            '.': 'TIE! 😐'
        }

    def random_move(self):
        while True:
            x, y = self.coords[randint(0, N * N - 1)]
            if self.states[x][y] != '.': continue
            return x, y

    def randomize(self):
        probs = [False, False, True, False, False]
        return (self.is_easy and choice(probs)) or choice(probs)

    def estimated_move(self):
        coords = self.possible_win()
        if coords and choice([True, False, True]):
            return coords

        if self.randomize():
            print('Randomized', end=' ')
            return self.random_move()

        move = None
        for i in range(N):
            for j in range(N):
                if self.states[i][j] != '.': continue

                e = self.evaluation(i, j)
                move = min(move, (e, (i, j))) if move else (e, (i, j))

        print('Estimated', end=' ')
        return move[1]

    def should_estimate(self):
        return self.steps <= (N * N) - 10 or (self.is_easy and choice([True, False]))

    def play(self):
        move_coords = ()
        while True:
            winner, win_coords = self.check_winner()
            self.draw_board(move_coords, win_coords)

            if winner:
                sleep(0.25)
                print('-' * self.val)
                print(f'{self.end_msg[winner]: ^{self.val}}')
                print('-' * self.val)
                return

            if self.player_turn == 'X':
                while True:
                    try:
                        idx = int(input('Your move: ')) - 1
                        if idx < 0: raise ValueError

                        x, y = self.coords[idx]
                        if self.states[x][y] != '.': raise IndexError

                        self.states[x][y] = 'X'
                        self.player_turn = 'O'
                        break
                    except (ValueError, IndexError):
                        print(f'{clr.RED}{"INVALID MOVE!":-^{self.val}}{clr.RESET}')
                    except KeyboardInterrupt:
                        print('Quit\n' + '-' * self.val)
                        print(f'{"LOSER!!😅": ^{self.val}}')
                        print('-' * self.val)
                        raise SystemExit
                    except SystemExit:
                        pass
            else:
                sleep(0.5)
                if self.should_estimate():
                    x, y = self.estimated_move()
                else:
                    _, x, y = self.min_ab(-2, 2)
                    print('Evaluated', end=' ')

                self.states[x][y] = 'O'
                self.player_turn = 'X'
                print('AI move:')

            move_coords = (x, y)
            self.steps += 1


if __name__ == "__main__":
    g = Game()
    if input('Select mode: ').lower() in ['1', 'easy']:
        g.is_easy = True
        print(f'Mode: {clr.GREEN}Easy\n')
    else:
        print(f'Mode: {clr.RED}Hard\n')
    g.play()
