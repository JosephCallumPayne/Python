import random
import copy
import os
import sys
import json
import base64

def running_in_idle():
    return 'idlelib.run' in sys.modules

def clear_screen():
    if running_in_idle():
        print("\n" * 100)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
    print_help()

class Game:
    def __init__(self, colours=7, guesses=8, code_length=4, custom_code=None):
        self.colours = colours
        self.guesses_left = guesses
        self.total_guesses = guesses
        self.code_length = code_length
        self.code = custom_code if custom_code else [random.randint(1, colours) for _ in range(code_length)]
        self.history = []
        self.status = "active"
        self.last_hint_index = -1

    def make_guess(self, guess):
        if self.status != "active":
            return f"Game already {self.status}.", self.status

        if len(guess) != self.code_length:
            return f"Invalid guess length. Expected {self.code_length} numbers.", None

        if self.guesses_left <= 0:
            return "No guesses left.", "lose"

        exact = []
        partial = []
        temp_code = copy.deepcopy(self.code)
        temp_guess = guess[:]

        for i in range(self.code_length):
            if temp_guess[i] == temp_code[i]:
                exact.append(1)
                temp_code[i] = -1
                temp_guess[i] = -2

        for g in temp_guess:
            if g in temp_code:
                partial.append(0)
                temp_code[temp_code.index(g)] = -1

        feedback = exact + partial
        self.history.append((guess, feedback))
        self.guesses_left -= 1

        if len(exact) == self.code_length:
            self.status = "won"
            return "🎉 Correct! You've cracked the code!", "win"

        if self.guesses_left == 0:
            self.status = "lost"
            return f"💀 Out of guesses! The code was {self.code}", "lose"

        return f"Feedback: {feedback} | Guesses left: {self.guesses_left}", None

    def summary(self):
        return (
            f"Guesses left: {self.guesses_left}/{self.total_guesses}, "
            f"Colours: {self.colours}, Code length: {self.code_length}, "
            f"Status: {self.status}"
        )


    def show_history(self):
        if not self.history:
            return "No guesses yet."
        return "\n".join([f"Guess: {guess} → Feedback: {feedback}" for guess, feedback in self.history])

    def show_solution(self):
        return self.code

    def give_hint(self):
        for i in range(self.code_length):
            if not any(g[i] == self.code[i] for g, _ in self.history):
                return f"💡 Hint: Position {i+1} is {self.code[i]}"
        return "No more hints available!"
    def to_seed(self):
        # Serialise current game state into a seed string
        history_str = "|".join([",".join(map(str, g)) + ":" + "".join(map(str, f)) for g, f in self.history])
        return f"{self.colours}-{self.guesses_left}-{self.code_length}-{'_'.join(map(str, self.code))}-{history_str}"



class GameManager:
    def __init__(self):
        self.games = {}
        self.current_game = None
        self.next_game_id = 1
        self.last_settings = (7, 8, 4)

    def create_game(self, colours, guesses, code_length):
        self.last_settings = (colours, guesses, code_length)
        game_id = self.next_game_id
        self.games[game_id] = Game(colours, guesses, code_length)
        self.current_game = game_id
        self.next_game_id += 1
        return game_id

    def create_custom_game(self, custom_code, colours, guesses):
        self.last_settings = (colours, guesses, len(custom_code))
        game_id = self.next_game_id
        self.games[game_id] = Game(colours, guesses, len(custom_code), custom_code)
        self.current_game = game_id
        self.next_game_id += 1
        return game_id

    def switch_game(self, game_id):
        if game_id in self.games:
            self.current_game = game_id
            return True
        return False

    def export_game_seed(self, game_id):
        game = self.games.get(game_id)
        if not game:
            return None

        data = {
            "colours": game.colours,
            "guesses_total": game.total_guesses,
            "guesses_left": game.guesses_left,
            "code": game.code,
            "length": game.code_length,
            "history": game.history,  # includes both guess and feedback
        }

        json_str = json.dumps(data)
        return base64.urlsafe_b64encode(json_str.encode()).decode()

    def import_game_from_seed(self, seed_str):
        try:
            decoded = base64.urlsafe_b64decode(seed_str.encode()).decode()
            data = json.loads(decoded)

            game = Game(
                colours=data["colours"],
                guesses=data["guesses_total"],
                code_length=data["length"],
                custom_code=data["code"]
            )
            game.guesses_left = data["guesses_left"]
            game.history = data["history"]

            # Determine win/loss if code is cracked or no guesses remain
            if game.guesses_left == 0:
                game.status = "lost"
            elif game.history and all(game.code[i] == g[i] for g, _ in game.history[-1:] for i in range(game.code_length)):
                game.status = "won"

            game_id = self.next_game_id
            self.games[game_id] = game
            self.current_game = game_id
            self.next_game_id += 1
            return game_id
        except Exception as e:
            print(f"❌ Failed to import seed: {e}")
            return None

    def generate_seed(self, code, colours=None, total_guesses=8, guesses_left=None):
        if not isinstance(code, list) or not all(isinstance(i, int) for i in code):
            print("❌ Invalid code format. Must be a list of integers.")
            return None

        max_digit = max(code)
        if colours is None:
            colours = max(7, max_digit)

        if guesses_left is None:
            guesses_left = total_guesses

        # Create temporary game instance (do NOT add to self.games)
        game = Game(colours, total_guesses, len(code), code)
        game.guesses_left = guesses_left
        game.history = []

        # Export seed from the temporary game without registering it
        data = {
            "colours": game.colours,
            "guesses_total": game.total_guesses,
            "guesses_left": game.guesses_left,
            "code": game.code,
            "length": game.code_length,
            "history": game.history,
        }

        json_str = json.dumps(data)
        return base64.urlsafe_b64encode(json_str.encode()).decode()

    def current(self):
        return self.games.get(self.current_game, None)

    def list_games(self):
        return [
            f"#{gid}: {game.summary()}" + (" [Active]" if gid == self.current_game else "")
            for gid, game in self.games.items()
        ]

    def remove_game(self, game_id):
        if game_id in self.games:
            self.games[game_id].status = "cancelled"
            print(f"Game #{game_id} has been cancelled. The solution was: {self.games[game_id].show_solution()}")
            if self.current_game == game_id:
                self._switch_to_next_available_game()

    def _switch_to_next_available_game(self):
        for gid in sorted(self.games):
            if self.games[gid].status == "active":
                self.current_game = gid
                print(f"Switched to game #{gid}")
                return
        self.current_game = None
        print("No active games remaining.")

    def replay_last(self):
        colours, guesses, length = self.last_settings
        return self.create_game(colours, guesses, length)

def print_help():
    help_text = """
    🎯 Welcome to Mastermind! Available commands:

    1. help                                → Show this help message.
    2. new <colours> <guesses> <length>    → Start a new game.
    3. new easy / new hard                 → Start preset games.
    4. custom [code] <colours> <guesses>   → Create a game with your own code.
    5. guess like 1,2,3,4                  → Submit a guess.
    6. history                             → Show the current game's guess history.
    7. games                               → List all games and their statuses.
    8. switch <id>                         → Switch to another game by ID.
    9. end <game_id>                       → Cancel a game and reveal its solution.
    10. solution <game_id>                 → Reveal the solution of a game.
    11. hint                               → Get a hint for the current game.
    12. replay                             → Replay the last game settings.
    13. exit                               → Exit the program.

    After exiting, type Mastermind() to play again.
    """
    print(help_text)

def Mastermind():
    manager = GameManager()
    print_help()

    while True:
        cmd = input(">> ").strip()

        if cmd == "exit":
            print("Goodbye!")
            return
        elif cmd == "clear":
            clear_screen()

        elif cmd == "help":
            print_help()

        elif cmd in ("new easy", "easy"):
            game_id = manager.create_game(6, 10, 3)
            print(f"🟢 Easy game #{game_id} started.")

        elif cmd in ("new hard", "hard"):
            game_id = manager.create_game(8, 6, 5)
            print(f"🔴 Hard game #{game_id} started.")

        elif cmd.startswith("new"):
            parts = cmd.split()
            try:
                colours = int(parts[1]) if len(parts) > 1 else 7
                guesses = int(parts[2]) if len(parts) > 2 else 8
                length = int(parts[3]) if len(parts) > 3 else 4
                game_id = manager.create_game(colours, guesses, length)
                print(f"Started game #{game_id}: Colours 1–{colours}, {guesses} guesses, Length {length}.")
            except ValueError:
                print("❌ Invalid format. Use: new [colours] [guesses] [length]")

        elif cmd.startswith("custom"):
            parts = cmd.split(None, 1)
            if len(parts) != 2:
                print("Usage: custom [code] [colours] [guesses] — e.g. custom [1,2,3,4] 7 8")
                continue
            try:
                args = parts[1].strip()
                tokens = args.split()

                code_str = tokens[0]
                custom_code = eval(code_str)
                if not isinstance(custom_code, list) or not all(isinstance(i, int) for i in custom_code):
                    raise ValueError("Code must be a list of integers.")

                colours = 7
                guesses = 8
                if len(tokens) == 2:
                    colours = int(tokens[1])
                elif len(tokens) == 3:
                    colours = int(tokens[1])
                    guesses = int(tokens[2])

                game_id = manager.create_custom_game(custom_code, colours, guesses)
                clear_screen()
                print(f"🎮 Custom game #{game_id} created with colours 1–{colours} and {guesses} guesses.")
            except Exception:
                print("❌ Invalid format. Example:\n  custom [1,2,3,4]       → defaults to 7 colours, 8 guesses\n  custom [1,2,3,3] 5     → 5 colours\n  custom [1,2,3,4] 8 10  → 8 colours, 10 guesses")

        elif cmd == "replay":
            game_id = manager.replay_last()
            print(f"🔁 Replayed settings. New game #{game_id} started.")

        elif cmd == "games":
            print("\n".join(manager.list_games()))

        elif cmd == "history":
            game = manager.current()
            print(game.show_history() if game else "No active game.")

        elif cmd.startswith("seed"):
            try:
                parts = cmd.split(None, 1)
                if len(parts) != 2:
                    print("Usage: seed <code> [colours] [guesses] [guesses_left]")
                    continue

                args = parts[1].split()
                code = list(map(int, args[0].split(",")))

                colours = int(args[1]) if len(args) > 1 else None
                total_guesses = int(args[2]) if len(args) > 2 else 8
                guesses_left = int(args[3]) if len(args) > 3 else total_guesses

                seed = manager.generate_seed(code, colours, total_guesses, guesses_left)
                print(f"🌱 Seed: {seed}")
            except Exception as e:
                print("❌ Invalid format. Use: seed 1,2,3,4 [colours] [guesses] [guesses_left]")

        elif cmd.startswith("export"):
            game = manager.current()
            if not game:
                print("❌ No active game.")
                continue
            seed = manager.export_game_seed(manager.current_game)
            print(f"📤 Exported Seed: {seed}")

        elif cmd.startswith("import"):
            try:
                seed = cmd.split(None, 1)[1]
                game_id = manager.import_game_from_seed(seed)
                if game_id:
                    print(f"📥 Game #{game_id} imported and resumed.")
                else:
                    print("❌ Failed to import game.")
            except IndexError:
                print("❌ Usage: import <seed>")

        elif cmd == "hint":
            game = manager.current()
            if game:
                print(game.give_hint())
            else:
                print("No active game.")

        elif cmd.startswith("solution"):
            parts = cmd.split()
            if len(parts) == 2 and parts[1].isdigit():
                gid = int(parts[1])
                game = manager.games.get(gid)
                if game:
                    print(f"The solution for game #{gid} is {game.show_solution()}")
                else:
                    print("Invalid game ID.")
            else:
                print("Usage: solution <game_id>")

        elif cmd.startswith("end"):
            parts = cmd.split()
            if len(parts) == 2 and parts[1].isdigit():
                gid = int(parts[1])
                if manager.games.get(gid):
                    print(f"Ending game #{gid}...")
                    manager.remove_game(gid)
                else:
                    print("Invalid game ID.")
            else:
                print("Usage: end <game_id>")

        elif cmd.startswith("switch"):
            parts = cmd.split()
            if len(parts) == 2 and parts[1].isdigit():
                gid = int(parts[1])
                if manager.switch_game(gid):
                    print(f"Switched to game #{gid}")
                    print(manager.current().show_history())
                else:
                    print("Invalid game ID.")
            else:
                print("Usage: switch <game_id>")

        else:
            game = manager.current()
            if not game:
                print("No active game. Start one with new, custom, or replay.")
                continue
            try:
                guess = list(map(int, cmd.split(',')))
                message, status = game.make_guess(guess)
                print(message)
                if status in ("win", "lose"):
                    print("🏁 Game Over.")
                    manager._switch_to_next_available_game()
            except ValueError:
                print("Invalid input. Use format like 1,2,3,4")

if __name__ == "__main__":
    Mastermind()
