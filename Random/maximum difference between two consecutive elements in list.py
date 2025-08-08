def max_consecutive_difference1(lst):
    if len(lst) < 2:
        return 0
    else:
        max_diff = 0
        for i in range(len(lst) - 1):
            diff = abs(lst[i] - lst[i + 1])
            if diff > max_diff:
                max_diff = diff
    
        return max_diff