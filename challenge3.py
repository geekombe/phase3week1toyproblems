def solution(N):
    for num_letters in range(26, 0, -1):
        if N % num_letters == 0:
            break
    repeat_count = N // num_letters

    result = ''.join(chr(ord('a') + i) * repeat_count for i in range(num_letters))

    return result
