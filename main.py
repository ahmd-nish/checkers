import tkinter as tk
import random
import checkers


class CheckersGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Control console")
        self.game = checkers.Game(loop_mode=True)
        self.game.setup()

        self.player_count_var = tk.IntVar(value=1)
        self.player1_name_var = tk.StringVar(value="Player 1")
        self.player2_name_var = tk.StringVar(value="Player 2")

        self.turn_label = tk.Label(self.root, text="Task processing frame")
        self.turn_label.pack()

        self.text_output = tk.Text(self.root, height=4, width=40)
        self.text_output.pack()

        self.player_count_label = tk.Label(self.root, text="Player Count:")
        self.player_count_label.pack()
        self.player_count_menu = tk.OptionMenu(self.root, self.player_count_var, 1, 2)
        self.player_count_menu.pack()

        self.player1_name_label = tk.Label(self.root, text="Player 1 Name:")
        self.player1_name_label.pack()
        self.player1_name_entry = tk.Entry(self.root, textvariable=self.player1_name_var)
        self.player1_name_entry.pack()

        self.player2_name_label = tk.Label(self.root, text="Player 2 Name:")
        self.player2_name_label.pack()
        self.player2_name_entry = tk.Entry(self.root, textvariable=self.player2_name_var)
        self.player2_name_entry.pack()

        self.coin_toss_button = tk.Button(self.root, text="Coin Toss", command=self.coin_toss)
        self.coin_toss_button.pack()

        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.pack()

        self.draw_button = tk.Button(self.root, text="Draw", command=self.offer_draw)
        self.draw_button.pack()

        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit_game)
        self.quit_button.pack()

        self.is_draw_offered = False


    def update_text_output(self, message):
        self.text_output.insert(tk.END, message + "\n")
        self.text_output.see(tk.END)

    def coin_toss(self):
        coin_side = random.choice(["Heads", "Tails"])
        if coin_side == "Heads":
            self.game.turn = checkers.RED
            self.update_text_output("Coin Toss: RED goes first")
        elif coin_side == "Tails":
            self.game.turn = checkers.BLUE
            self.update_text_output("Coin Toss: BLUE goes first")

    def offer_draw(self):
        self.is_draw_offered = True
        self.update_text_output("Draw offered. Both players need to agree.")


    def handle_draw(self):
        self.update_text_output("Draw! The game ends in a draw.")
        self.game.is_game_over = True

    def start_game(self):
        player_count = self.player_count_var.get()
        player1_name = self.player1_name_var.get()
        player2_name = self.player2_name_var.get()

        self.update_text_output("Game started.")

        if player_count == 1:
            player2_name = "AI"
        # Randomly select player colors
        name = [player1_name, player2_name]
        random.shuffle(name)

        self.game.setup()
        while not self.game.check_for_endgame():
            if self.is_draw_offered:
                self.handle_draw()
                break

            if self.game.turn == checkers.RED:
                self.update_text_output(f"Turn: {name[0]} (RED)\n")
                self.game.player_turn()
            if self.game.turn == checkers.BLUE:
                self.update_text_output(f"Turn: {name[1]} (BLUE)\n")
                self.game.player_turn()

            self.game.update()

            if self.game.check_for_endgame():
                self.update_text_output("You can quit or play another game!")
                break

            self.root.update()  # Update the GUI interface

    def quit_game(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    gui = CheckersGUI()
    gui.run()