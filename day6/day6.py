def solve():
    races = [
        (44806572,208158110501102),
       
    ]
    output = 1
    for race in races:
        count = 0
        for i in range(1,race[0]):
            # print('here')
            speed = i
            distance = speed * (race[0]-i)
            # print(distance ,race[1])
            if distance > race[1]:
                # print(speed)
                count += 1
        output *= count
        # print(race)
    print(output)
print(solve())