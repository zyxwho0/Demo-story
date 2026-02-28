import tkinter as tk
from tkinter import font
import random
from enum import Enum

class Move(Enum):
    ROCK = "🪨"
    SCISSORS = "✂️"

class GameResult(Enum):
    WIN = "win"
    LOSE = "lose"
    DRAW = "draw"

class RockScissorsGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock vs Scissors")
        self.root.geometry("600x700")
        self.root.configure(bg="#1a1a2e")
        
        # Game state
        self.player_score = 0
        self.computer_score = 0
        self.draw_score = 0
        
        # Custom fonts
        self.title_font = font.Font(family="Helvetica", size=32, weight="bold")
        self.subtitle_font = font.Font(family="Helvetica", size=11)
        self.label_font = font.Font(family="Helvetica", size=9, weight="bold")
        self.score_font = font.Font(family="Helvetica", size=24, weight="bold")
        self.emoji_font = font.Font(family="Helvetica", size=48)
        self.vs_font = font.Font(family="Helvetica", size=20, weight="bold")
        self.result_font = font.Font(family="Helvetica", size=18, weight="bold")
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the GUI components"""
        # Main container
        main_frame = tk.Frame(self.root, bg="#1a1a2e")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="Rock vs Scissors",
            font=self.title_font,
            bg="#1a1a2e",
            fg="#f5a623"
        )
        title_label.pack(pady=(0, 5))
        
        # Subtitle
        subtitle_label = tk.Label(
            main_frame,
            text="Pick your move – Rock beats Scissors!",
            font=self.subtitle_font,
            bg="#1a1a2e",
            fg="#aaa"
        )
        subtitle_label.pack(pady=(0, 20))
        
        # Scoreboard
        scoreboard_frame = tk.Frame(main_frame, bg="#1a1a2e")
        scoreboard_frame.pack(pady=15)
        
        self.score_labels = {}
        for i, (key, label, color) in enumerate([
            ("player", "You", "#f5a623"),
            ("draws", "Draws", "#aaa"),
            ("computer", "Computer", "#e94560")
        ]):
            score_box = tk.Frame(
                scoreboard_frame,
                bg="#2a2a4e",
                relief=tk.FLAT,
                bd=0,
                highlightthickness=1,
                highlightbackground="#444"
            )
            score_box.pack(side=tk.LEFT, padx=15)
            
            label_widget = tk.Label(
                score_box,
                text=label,
                font=self.label_font,
                bg="#2a2a4e",
                fg="#aaa"
            )
            label_widget.pack(pady=(8, 5))
            
            value_widget = tk.Label(
                score_box,
                text="0",
                font=self.score_font,
                bg="#2a2a4e",
                fg=color
            )
            value_widget.pack(pady=(0, 8), padx=20)
            
            self.score_labels[key] = value_widget
        
        # Choices buttons
        choices_frame = tk.Frame(main_frame, bg="#1a1a2e")
        choices_frame.pack(pady=20)
        
        self.rock_btn = tk.Button(
            choices_frame,
            text="🪨\nRock",
            font=("Helvetica", 14),
            bg="#1a3a52",
            fg="#fff",
            relief=tk.FLAT,
            bd=0,
            padx=25,
            pady=15,
            cursor="hand2",
            command=lambda: self.play("rock"),
            activebackground="#2a5a82",
            activeforeground="#fff"
        )
        self.rock_btn.pack(side=tk.LEFT, padx=10)
        
        self.scissors_btn = tk.Button(
            choices_frame,
            text="✂️\nScissors",
            font=("Helvetica", 14),
            bg="#1a3a52",
            fg="#fff",
            relief=tk.FLAT,
            bd=0,
            padx=20,
            pady=15,
            cursor="hand2",
            command=lambda: self.play("scissors"),
            activebackground="#2a5a82",
            activeforeground="#fff"
        )
        self.scissors_btn.pack(side=tk.LEFT, padx=10)
        
        # Arena
        arena_frame = tk.Frame(main_frame, bg="#1a1a2e")
        arena_frame.pack(pady=20)
        
        # Player icon
        player_frame = tk.Frame(arena_frame, bg="#1a1a2e")
        player_frame.pack(side=tk.LEFT, padx=20)
        
        self.player_icon = tk.Label(
            player_frame,
            text="❓",
            font=self.emoji_font,
            bg="#1a1a2e",
            fg="#fff"
        )
        self.player_icon.pack()
        
        player_name = tk.Label(
            player_frame,
            text="You",
            font=self.label_font,
            bg="#1a1a2e",
            fg="#aaa"
        )
        player_name.pack()
        
        # VS
        vs_label = tk.Label(
            arena_frame,
            text="VS",
            font=self.vs_font,
            bg="#1a1a2e",
            fg="#555"
        )
        vs_label.pack(side=tk.LEFT, padx=15)
        
        # Computer icon
        computer_frame = tk.Frame(arena_frame, bg="#1a1a2e")
        computer_frame.pack(side=tk.LEFT, padx=20)
        
        self.computer_icon = tk.Label(
            computer_frame,
            text="❓",
            font=self.emoji_font,
            bg="#1a1a2e",
            fg="#fff"
        )
        self.computer_icon.pack()
        
        computer_name = tk.Label(
            computer_frame,
            text="Computer",
            font=self.label_font,
            bg="#1a1a2e",
            fg="#aaa"
        )
        computer_name.pack()
        
        # Result banner
        self.result_banner = tk.Label(
            main_frame,
            text="",
            font=self.result_font,
            bg="#1a1a2e",
            fg="#aaa"
        )
        self.result_banner.pack(pady=20, min_height=40)
        
        # Reset button
        reset_btn = tk.Button(
            main_frame,
            text="Reset Scores",
            font=("Helvetica", 10, "bold"),
            bg="#e94560",
            fg="#fff",
            relief=tk.FLAT,
            bd=0,
            padx=20,
            pady=8,
            cursor="hand2",
            command=self.reset_scores,
            activebackground="#d43550",
            activeforeground="#fff"
        )
        reset_btn.pack(pady=10)
    
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
            return
        
        computer_move = self.get_computer_move()
        result = self.get_result(player_move, computer_move)
        
        # Update icons
        self.player_icon.config(text=player_move.value)
        self.computer_icon.config(text=computer_move.value)
        
        # Animate shake
        self.shake_animation(self.player_icon)
        self.shake_animation(self.computer_icon)
        
        # Update scores and result
        if result == GameResult.WIN:
            self.player_score += 1
            outcome = "🎉 You Win!"
            color = "#f5a623"
        elif result == GameResult.LOSE:
            self.computer_score += 1
            outcome = "💀 Computer Wins!"
            color = "#e94560"
        else:
            self.draw_score += 1
            outcome = "🤝 It's a Draw!"
            color = "#aaa"
        
        # Update result banner
        self.result_banner.config(text=outcome, fg=color)
        
        # Update scores
        self.score_labels["player"].config(text=str(self.player_score))
        self.score_labels["computer"].config(text=str(self.computer_score))
        self.score_labels["draws"].config(text=str(self.draw_score))
    
    def shake_animation(self, widget):
        """Simple shake animation"""
        original_fg = widget.cget("fg")
        widget.config(fg="#f5a623")
        self.root.after(200, lambda: widget.config(fg=original_fg))
    
    def reset_scores(self):
        """Reset all scores to zero"""
        self.player_score = 0
        self.computer_score = 0
        self.draw_score = 0
        
        self.score_labels["player"].config(text="0")
        self.score_labels["computer"].config(text="0")
        self.score_labels["draws"].config(text="0")
        
        self.player_icon.config(text="❓")
        self.computer_icon.config(text="❓")
        self.result_banner.config(text="", fg="#aaa")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockScissorsGameGUI(root)
    root.mainloop()
