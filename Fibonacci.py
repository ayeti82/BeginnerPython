def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_iter(n):
    a, b = 0, 1
    for i in range(1, n-1):
        temp = a + b
        a = b
        b = temp
    return b


if __name__ == '__main__':
    print("Enter a number to find it's fibonacci number:")
    num = int(input())
    print("The fibonacci number using recursion is:", fib(num))
    print("The fibonacci number using iteration is:", fib_iter(num))
