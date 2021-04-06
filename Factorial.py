def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)


def fac_iter(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


if __name__ == '__main__':
    print("Enter a number to find it's factorial:")
    num = int(input())
    print("The factorial using recursion is:", fac(num))
    print("The factorial using iteration is:", fac_iter(num))
