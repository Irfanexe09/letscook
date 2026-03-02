"""
Tic Tac Toe Game
A simple command-line implementation of Tic Tac Toe with Player vs AI
"""

import random


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board as a list
        self.current_player = 'X'
    
    def print_board(self):
        """Display the game board"""
        print('\n')
        for i in range(3):
            print(f" {self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]} ")
            if i < 2:
                print("-----------")
        print('\n')
    
    def print_board_positions(self):
        """Show the board with position numbers for reference"""
        print('\nPosition numbers:')
        for i in range(3):
            print(f" {i*3} | {i*3+1} | {i*3+2} ")
            if i < 2:
                print("-----------")
        print()
    
    def is_winner(self, player):
        """Check if the given player has won"""
        # Winning combinations
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for pattern in win_patterns:
            if all(self.board[i] == player for i in pattern):
                return True
        return False
    
    def is_board_full(self):
        """Check if the board is full"""
        return ' ' not in self.board
    
    def get_available_moves(self):
        """Return list of available positions"""
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def make_move(self, position, player):
        """Place a player's mark on the board"""
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False
    
    def ai_move(self):
        """Simple AI strategy: try to win, block opponent, or pick random"""
        available = self.get_available_moves()
        
        # Try to win
        for move in available:
            self.board[move] = 'O'
            if self.is_winner('O'):
                return move
            self.board[move] = ' '
        
        # Try to block player
        for move in available:
            self.board[move] = 'X'
            if self.is_winner('X'):
                self.board[move] = ' '
                return move
            self.board[move] = ' '
        
        # Take center if available
        if 4 in available:
            return 4
        
        # Take a corner
        corners = [0, 2, 6, 8]
        corner_moves = [c for c in corners if c in available]
        if corner_moves:
            return random.choice(corner_moves)
        
        # Random move
        return random.choice(available)
    
    def play(self):
        """Main game loop"""
        print("=" * 30)
        print("  WELCOME TO TIC TAC TOE!")
        print("=" * 30)
        print("\nYou are 'X' and AI is 'O'")
        self.print_board_positions()
        
        while True:
            self.print_board()
            
            # Player's turn
            while True:
                try:
                    position = int(input("Enter position (0-8): "))
                    if 0 <= position <= 8:
                        if self.make_move(position, 'X'):
                            break
                        else:
                            print("That position is already taken!")
                    else:
                        print("Please enter a number between 0 and 8.")
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 8.")
            
            # Check if player won
            if self.is_winner('X'):
                self.print_board()
                print("🎉 You won! Congratulations! 🎉")
                break
            
            # Check if board is full
            if self.is_board_full():
                self.print_board()
                print("It's a draw!")
                break
            
            # AI's turn
            print("AI is thinking...")
            ai_position = self.ai_move()
            self.make_move(ai_position, 'O')
            print(f"AI played position {ai_position}")
            
            # Check if AI won
            if self.is_winner('O'):
                self.print_board()
                print("AI won! Better luck next time.")
                break
            
            # Check if board is full
            if self.is_board_full():
                self.print_board()
                print("It's a draw!")
                break


def main():
    while True:
        game = TicTacToe()
        game.play()
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
