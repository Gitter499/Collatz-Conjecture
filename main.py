def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False


def main():
    n = int(input("Enter some number \n"))
    find_num(n)


def find_num(n):
    if not isEven(n):
        n = (n * 3) + 1
    else:
        n /= 2
    print(n)
    find_num(n)


if __name__ == "__main__":
    main()
