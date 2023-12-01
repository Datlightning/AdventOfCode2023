def getStart(string):
    nums = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
    }
    first = "failure"
    last = 0
    currentword = ""
    for s in range(len(string)):
        try:
            int(string[s])
            first = string[s]
            break
        except:
            currentword += string[s]
            for key in nums.keys():
                if(key in currentword):
                    first = nums[key]
                    break
        if(first != "failure"):
            break
    currentword = ""
    for s in list(range(len(list(string))))[::-1]:
        try:
            int(string[s])
            last = string[s]
            break
        except:
            currentword = string[s] + currentword
            for key in nums.keys():
                if(key in currentword):
                    last = nums[key]
                    break
        if(last != 0):
            break
    return int(f"{first}{last}")

def solve():
    lines = []
    sum = 0
    with open("day1/input.txt", "r") as file:
        lines = file.read().split("\n")
    for line in lines:
        print(getStart(line))
        sum += getStart(line)
    return sum
