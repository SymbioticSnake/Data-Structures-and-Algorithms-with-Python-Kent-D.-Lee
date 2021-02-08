def factorial(n):
    # Base case
    if n == 0:
        return 1
    
    # Recursive case
    return n * factorial(n-1)

def main():
    print(factorial(5))
    print(factorial(0))
    print(factorial(1))

if __name__ == "__main__": main()