def evaluate_hand(hand):
    data = {}
    cards = set()
    for h in hand:
        if not h in cards:
            data[h] = 0
            cards.add(h)
        data[h] += 1
        if data[h] == 5:
            return "Five"
        if data[h] == 4:
            return "Four"
    length = len(data)
    match length:
        case 2:
            return "Full"
        case 3:
            for card, value in data.items():
                if value == 3:
                    return "Three"
                if value == 2:
                    return "Two"
        case 4:
            return "One"
    return "High"
def get_value(card):
    values = {
            "A":13,
            "K":12,
            "Q":11,
            "J":10,
            "T":9,
            "9":8,
            "8":7,
            "7":6,
            "6":5,
            "5":4,
            "4":3,
            "3":2,
            "2":1
        }
    try:
        return values[card]
    except:
        return -1
def solve():
    lines = []
    with open("day7/input7.txt") as file:
        lines = file.read().split("\n")
    hands = {
        "One":[],
        "Two":[],
        "Three":[],
        "Four":[],
        "Five":[],
        "Full":[],
        "High":[]
    }
    possible_hands = [
        "High",
        "One",
        "Two",
        "Three",
        "Full",
        "Four",
        "Five"
    ]
        

   
    for line in lines:
        split_line = line.split(" ")
        hand = split_line[0]
        bet = split_line[1]
        current_list = hands[evaluate_hand(hand)]
        if current_list == 0:
            current_list.append((hand, bet))
        index = 0
        for index, item in enumerate(current_list):
            if get_value(hand[0]) < get_value(item[0][0]):
                break
            if get_value(hand[0]) > get_value(item[0][0]):
                break
            if get_value(hand[0]) == get_value(item[0][0]):
                i = 0                
                while get_value(hand[i]) == get_value(item[0][i]):
                    i+=1
                if get_value(hand[i]) < get_value(item[0][i]):
                     break
                else:
                    index += 1
                    break 
        current_list.insert(index, (hand, bet))
    total_score = 0
    current_index = 1
    for hand_type in possible_hands:
        for card in hands[hand_type]:
            total_score += current_index * card[1]
            current_index += 1
    return total_score
print(solve())
        

        
