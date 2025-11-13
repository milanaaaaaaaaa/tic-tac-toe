from game_logic import Game
from display import print_board

def main():
    print("🎮 Добро пожаловать в игру 'Крестики-нолики'!")
    print("Игрок 1: X | Игрок 2: O")
    print()

    game = Game()
    current_player = "X"

    while True:
        print_board(game.board)
        try:
            move = int(input(f"Ход игрока {current_player}. Введите номер клетки (1-9): ")) - 1
            if move < 0 or move > 8:
                print("❌ Неверный номер клетки. Попробуйте снова.")
                continue
            if game.make_move(move, current_player):
                if game.check_winner(current_player):
                    print_board(game.board)
                    print(f"🎉 Игрок {current_player} победил!")
                    break
                elif game.is_board_full():
                    print_board(game.board)
                    print("🤝 Ничья!")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("❌ Клетка занята. Попробуйте снова.")
        except ValueError:
            print("❌ Введите число от 1 до 9.")

if __name__ == "__main__":
    main()
