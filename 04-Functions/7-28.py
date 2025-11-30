def f(dice):
    streak = 0
    streak_check = 0
    bufor = dice[0]
    int_streak = ''
    for char in dice:
        if char == bufor:
            streak+=1
        else:
            streak = 0
        if streak>=streak_check:
            streak_check = streak
            int_streak = char
        bufor = char
    return int_streak

if __name__ == "__main__":
    print(f('451117171'))