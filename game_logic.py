class Game:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # Поле 3x3 в виде списка

    def make_move(self, position, player):
        """Поставить символ игрока на позицию, если она свободна."""
        if self.board[position] == " ":
            self.board[position] = player
            return True
        return False

    def check_winner(self, player):
        """Проверить, выиграл ли игрок."""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # строки
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # столбцы
            [0, 4, 8], [2, 4, 6]              # диагонали
        ]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def is_board_full(self):
        """Проверить, заполнено ли поле."""
        return " " not in self.board

# Логика игры реализована
