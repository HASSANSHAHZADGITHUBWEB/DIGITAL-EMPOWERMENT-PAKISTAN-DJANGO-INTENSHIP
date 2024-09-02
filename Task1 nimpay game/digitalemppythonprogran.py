import sys

class NimGame:
    def __init__(self, num_red, num_blue, version='standard', first_player='computer', depth=3):
        self.num_red = num_red
        self.num_blue = num_blue
        self.version = version
        self.current_player = first_player
        self.depth = depth

    def is_game_over(self):
        return self.num_red == 0 or self.num_blue == 0

    def get_score(self):
        return self.num_red * 2 + self.num_blue * 3

    def human_move(self):
        while True:
            print(f"Current state - Red: {self.num_red}, Blue: {self.num_blue}")
            try:
                r = int(input("Enter number of red marbles to take: "))
                b = int(input("Enter number of blue marbles to take: "))
                if (0 <= r <= 2) and (0 <= b <= 2) and (r + b > 0) and (r <= self.num_red) and (b <= self.num_blue):
                    self.num_red -= r
                    self.num_blue -= b
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Please enter valid numbers.")

    def computer_move(self):
        best_score = float('-inf')
        best_move = None

        for move in self.get_valid_moves():
            r, b = move
            next_state = NimGame(self.num_red - r, self.num_blue - b, self.version, depth=self.depth - 1)
            score = self.minmax(next_state, False, float('-inf'), float('inf'))

            if score > best_score:
                best_score = score
                best_move = move

        r, b = best_move
        print(f"Computer takes {r} red and {b} blue marbles.")
        self.num_red -= r
        self.num_blue -= b

    def minmax(self, state, maximizing, alpha, beta):
        if state.is_game_over() or state.depth == 0:
            return state.evaluate()

        if maximizing:
            max_eval = float('-inf')
            for move in state.get_valid_moves():
                r, b = move
                next_state = NimGame(state.num_red - r, state.num_blue - b, state.version, depth=state.depth - 1)
                eval = self.minmax(next_state, False, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for move in state.get_valid_moves():
                r, b = move
                next_state = NimGame(state.num_red - r, state.num_blue - b, state.version, depth=state.depth - 1)
                eval = self.minmax(next_state, True, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def evaluate(self):
        if self.version == 'standard':
            if self.is_game_over():
                return -float('inf') if self.current_player == 'human' else float('inf')
        else:  # Misère version
            if self.is_game_over():
                return float('inf') if self.current_player == 'human' else -float('inf')
        return self.get_score()

    def get_valid_moves(self):
        moves = []
        for r in range(3):
            for b in range(3):
                if (r + b > 0) and (r <= self.num_red) and (b <= self.num_blue):
                    moves.append((r, b))
        if self.version == 'misere':
            return moves[::-1]
        return moves

    def play(self):
        while not self.is_game_over():
            if self.current_player == 'human':
                self.human_move()
                self.current_player = 'computer'
            else:
                self.computer_move()
                self.current_player = 'human'

        print("Game Over!")
        if self.version == 'standard':
            print("You lose!" if self.current_player == 'human' else "You win!")
        else:
            print("You win!" if self.current_player == 'human' else "You lose!")

        print(f"Final Score: Red: {self.num_red}, Blue: {self.num_blue}")
        print(f"Total Score: {self.get_score()}")

if __name__ == "__main__":
    num_red = int(input("Enter number of red marbles: "))
    num_blue = int(input("Enter number of blue marbles: "))
    version = input("Enter game version (standard/misere): ").lower()
    first_player = input("Who plays first (human/computer): ").lower()
    depth = int(input("Enter search depth for AI (optional, press enter for default): ") or 3)

    game = NimGame(num_red, num_blue, version, first_player, depth)
    game.play()
