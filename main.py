is_even = lambda n: True if n % 2 == 0 else False

nums_arr = []
recursion_error = False


def find_num(n):
    global limit
    nums_arr.append(n)
    try:
        if not is_even(n):
            n = (n * 3) + 1
        else:
            n /= 2
        
        nums_arr.append(n)
        if recursion_error:
            if n == 4:
                (evens, odds) = evens_odds_stats()
                evens = list(dict.fromkeys(evens))
                odds = list(dict.fromkeys(odds))
                print(
                    f"Congrats! You just ran all the numbers before the death loop! \nHere are your stats: \nEven numbers: {evens} \nOdd numbers: {odds} \n Sum of all first digits {first_digit_sum()}"
                )
                return
        print(n)
        find_num(n)
    except RecursionError:
        (evens, odds) = evens_odds_stats()
        evens = list(dict.fromkeys(evens))
        odds = list(dict.fromkeys(odds))
        print(
            f"Congrats! You just hit the Python recursion limit! \nHere are your stats: \nEven numbers: {evens} \nOdd numbers: {odds} \nSum of all first digits {first_digit_sum()}"
        )


def evens_odds_stats():
    evens_arr = []
    odds_arr = []
    for num in nums_arr:
        if is_even(num):
            if num == 2 or num == 4:
                return (evens_arr, odds_arr)
            else:
                evens_arr.append(num)
        else:
            if num == 2 or num == 4:
                return (evens_arr, odds_arr)
            else:
                odds_arr.append(num)
    evens_arr = list(dict.fromkeys(evens_arr))
    odds_arr = list(dict.fromkeys(odds_arr))
    return (evens_arr, odds_arr)


def first_digit_sum():
    sum = 0
    for num in nums_arr:
        sum += int(str(num)[:1])
    return sum


def main():
    global recursion_error
    print(
        "Welcome to a simple program that walks through the 3N+1 math problem")
    opt = input("Do you want to hit the Python RecursionError? [y/n] \n")
    if opt.lower()[0] == 'n':
        recursion_error = True
    elif opt.lower()[0] == 'y':
        recursion_error = False
    else:
        print("Invalid input")
    n = input("Enter some number \n")
    find_num(int(n))


if __name__ == "__main__":
    main()
