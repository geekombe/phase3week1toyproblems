def solution(A):
    total_bricks = sum(A)
    N = len(A)
    if total_bricks != 10 * N:
        return -1
    moves = 0
    balance = 0
    for bricks in A:
        balance += bricks - 10
        moves += abs(balance)
        print(moves)
    return moves


