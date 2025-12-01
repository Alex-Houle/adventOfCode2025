with open("input.txt", "r") as file:
    dial = 50
    zero = 0

    for line in file:
        line = line.strip()
        dir = line[0]
        num = int(line[1:])

        if dir == "R":
            dial = (dial + num) % 100
        else:
            dial = (dial - num) % 100

        if dial == 0:
            zero += 1

    print(zero)
