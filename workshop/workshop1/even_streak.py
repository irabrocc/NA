def even_streak(numbers):
    max_streak = 0
    current_streak = 0

    for number in numbers:
        if number % 2 == 0:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0

    return max_streak

print(even_streak([1,4,6,1,1,8,0,6,4,3,3,3]))