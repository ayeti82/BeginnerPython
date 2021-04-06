def print_lower_pattern(r):
    for i in range(1, r + 1):
        print(i * '* ', end=" ")
        print()


def print_upper_pattern(r):
    for i in range(r, 0, -1):
        print(i * '* ', end=" ")
        print()


if __name__ == '__main__':
    print("Enter number of rows: ")
    rows = int(input())
    print("Lower/Upper -> Enter T/F")
    flag = input().lower()
    if flag == 't':
        print_lower_pattern(rows)
    elif flag == 'f':
        print_upper_pattern(rows)
    else:
        print("Invalid command")
