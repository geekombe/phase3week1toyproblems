def digit_sum(n):
    return sum(int(digit) for digit in str(abs(n)))

def solution(A):
    digit_sum_map = {}
    
    for number in A:
        sum_digits = digit_sum(number)
        
        if sum_digits not in digit_sum_map:
            digit_sum_map[sum_digits] = [number]
        else:
            digit_sum_map[sum_digits].append(number)
            digit_sum_map[sum_digits].sort(reverse=True)
            if len(digit_sum_map[sum_digits]) > 2:
                digit_sum_map[sum_digits] = digit_sum_map[sum_digits][:2]
        max_sum = -1
    for numbers in digit_sum_map.values():
        if len(numbers) == 2:
            max_sum = max(max_sum, sum(numbers))
    print(max_sum)
    return max_sum
