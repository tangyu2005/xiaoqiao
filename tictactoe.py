#!/usr/bin/env python3
"""命令行三子棋（井字棋）游戏。"""

from __future__ import annotations


BOARD_SIZE = 3


def create_board() -> list[list[str]]:
    return [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def print_board(board: list[list[str]]) -> None:
    print("\n  1   2   3")
    for i, row in enumerate(board, start=1):
        print(f"{i} " + " | ".join(row))
        if i < BOARD_SIZE:
            print(" ---+---+---")
    print()


def check_winner(board: list[list[str]], player: str) -> bool:
    for i in range(BOARD_SIZE):
        if all(board[i][j] == player for j in range(BOARD_SIZE)):
            return True
        if all(board[j][i] == player for j in range(BOARD_SIZE)):
            return True

    if all(board[i][i] == player for i in range(BOARD_SIZE)):
        return True
    if all(board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)):
        return True

    return False


def is_draw(board: list[list[str]]) -> bool:
    return all(cell != " " for row in board for cell in row)


def get_move(player: str, board: list[list[str]]) -> tuple[int, int]:
    while True:
        raw = input(f"玩家 {player} 请输入落子坐标（行 列，如 2 3）：").strip()
        parts = raw.split()

        if len(parts) != 2 or not all(part.isdigit() for part in parts):
            print("输入格式不正确，请输入两个数字，例如：2 3")
            continue

        row, col = (int(parts[0]) - 1, int(parts[1]) - 1)
        if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
            print("坐标超出范围，请输入 1 到 3 之间的数字。")
            continue

        if board[row][col] != " ":
            print("该位置已被占用，请重新选择。")
            continue

        return row, col


def main() -> None:
    board = create_board()
    current_player = "X"

    print("欢迎来到三子棋！玩家 X 和玩家 O 轮流落子。")

    while True:
        print_board(board)
        row, col = get_move(current_player, board)
        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 玩家 {current_player} 获胜！")
            break

        if is_draw(board):
            print_board(board)
            print("平局！")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
