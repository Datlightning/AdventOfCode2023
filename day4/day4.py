
def bounds(cell, lines):
    return cell[0] < len(lines) and cell[0] >= 0 and cell[1] < len(lines[1]) and cell[1] >= 0

def is_number(cell, lines):
    numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    return lines[cell[0]][cell[1]] in numbers

def solve():
    lines = []
    with open("day4/input4.txt", "r") as file:
        lines = file.read().split("\n")
    cards = []
    for line in lines:
        cards.append(line.split(":")[1].strip().split("|"))
    total_sum = 0
    wins = 0
    cards_dict = {
        1:1
    }
    for i, y in enumerate(cards, start=1):
        cards_dict[i] = 1
    sum = 0
    for i, card in enumerate(cards, start=1):
            for x in range(cards_dict[i]):
                answers = set(card[0].split(" "))
                my_card = set(card[1].split(" "))
                answers.remove("")
                my_card.remove("")
                total_sum += int(2**(len(my_card.intersection(answers))-1))
                for number in range(int(len(my_card.intersection(answers)))):
                    cards_dict[i + number + 1] += 1
                # print(cards_dict)
            sum += cards_dict[i]



    return sum
    
#5833065
print(solve())