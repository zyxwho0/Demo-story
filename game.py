import random
from enum import Enum

class Move(Enum):
    ROCK = "🪨"
    SCISSORS = "✂️"

class GameResult(Enum):
    WIN = "win"
    LOSE = "lose"
    DRAW = "draw"

class RockScissorsGame:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.draw_score = 0
    
    def get_computer_move(self):
        """Randomly select a move for the computer"""
        return random.choice(list(Move))
    
    def get_result(self, player_move, computer_move):
        """Determine the game result"""
        if player_move == computer_move:
            return GameResult.DRAW
        if player_move == Move.ROCK and computer_move == Move.SCISSORS:
            return GameResult.WIN
        if player_move == Move.SCISSORS and computer_move == Move.ROCK:
            return GameResult.LOSE
        return GameResult.DRAW
    
    def play(self, player_move_name):
        """Play a single round"""
        try:
            player_move = Move[player_move_name.upper()]
        except KeyError:
            print(f"Invalid move: {player_move_name}. Choose 'rock' or 'scissors'.")
            return
        
        computer_move = self.get_computer_move()
        result = self.get_result(player_move, computer_move)
        
        # Update scores
        if result == GameResult.WIN:
            self.player_score += 1
            outcome = "🎉 You Win!"
        elif result == GameResult.LOSE:
            self.computer_score += 1
            outcome = "💀 Computer Wins!"
        else:
            self.draw_score += 1
            outcome = "🤝 It's a Draw!"
        
        # Display round result
        self.display_round(player_move, computer_move, outcome)
    
    def display_round(self, player_move, computer_move, outcome):
        """Display the results of a single round"""
        print(f"\n{player_move.value} vs {computer_move.value}")
        print(outcome)
        print(f"Score: You {self.player_score} | Draws {self.draw_score} | Computer {self.computer_score}")
    
    def display_scoreboard(self):
        """Display the current scoreboard"""
        print("\n" + "="*50)
        print("ROCK vs SCISSORS - Scoreboard")
        print("="*50)
        print(f"You:      {self.player_score}")
        print(f"Draws:    {self.draw_score}")
        print(f"Computer: {self.computer_score}")
        print("="*50 + "\n")
    
    def reset_scores(self):
        """Reset all scores to zero"""
        self.player_score = 0
        self.computer_score = 0
        self.draw_score = 0
        print("Scores have been reset!")
    
    def run(self):
        """Run the game in interactive mode"""
        print("\n🎮 Welcome to Rock vs Scissors!")
        print("Type 'rock' or 'scissors' to play, 'score' to see scores, 'reset' to clear, or 'quit' to exit.\n")
        
        while True:
            user_input = input("Your move: ").strip().lower()
            
            if user_input == 'quit':
                print("Thanks for playing! Final scores:")
                self.display_scoreboard()
                break
            elif user_input == 'score':
                self.display_scoreboard()
            elif user_input == 'reset':
                self.reset_scores()
            elif user_input in ['rock', 'scissors']:
                self.play(user_input)
            else:
                print("Invalid input. Please enter 'rock', 'scissors', 'score', 'reset', or 'quit'.")

if __name__ == "__main__":
    game = RockScissorsGame()
    game.run()
