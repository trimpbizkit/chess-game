from gamestate import GameState, Player
from notation import validate_file_first_board_position

def run_game_loop(state):
    turn_counter = 0
    state.print_state()
    while True:
        player_move = input("Enter move: ")
        try:
            validate_file_first_board_position(player_move)
        except ValueError as e:
            print(f"Move invalid, try again: {e}\n")
            continue
        if state.turn == Player.WHITE:
            turn_counter += 1 # each time it is White to move, increment
        if state.turn == Player.BLACK:
            pass
        state.change_turn()
        state.print_state()

def main():
    state = GameState()
    try:
        run_game_loop(state)
    except KeyboardInterrupt:
        print("\nGame cancelled by interrupt")

if __name__ == "__main__":
    main()
