def sum_natural(n):
    if n == 0 or n == 1:
        return 1
    if n > 1:
        n += sum_natural(n-1)
    return n
if __name__ == "__main__":
    print(sum_natural(5))