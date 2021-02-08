memo = {}


def fib(n):
    if n in memo:
        return memo[n]

    if n == 0:
        memo[0] = 0
        return 0

    if n == 1:
        memo[1] = 1
        return 1

    val = fib(n-1) + fib(n-2)
    memo[n] = val

    return val


def main():
    print(fib(100))


if __name__ == "__main__":
    main()
