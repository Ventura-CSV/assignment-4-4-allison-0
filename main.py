def main():

    numbers = []
    for i in range(5):
        number = float(input(f"Enter number {i+1}: "))
        numbers.append(number)

    print(*numbers)
    print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
