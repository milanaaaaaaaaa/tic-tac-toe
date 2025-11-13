def print_board(board):
    """Вывести игровое поле в консоль."""
    print("-------------")
    for i in range(0, 9, 3):
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
        print("-------------")
