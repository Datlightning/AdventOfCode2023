import random as r
def evaluate_joker(data):
    jokers = data["J"]
    length = len(data)
    match jokers:
        case 5:
            return "Five"
        case 4:
            return "Five"
        case 3:
            match length:
                case 2:
                    return "Five"
                case 3: 
                    return "Four"
        case 2:
            match length:
                case 2:
                    return "Five"
                case 3:
                    return "Four"
                case 4: 
                    return "Three"
        case 1:
            match length:
                case 2:
                    return "Five"
                case 3:
                    for card, value in data.items():
                        if value == 3:
                            return "Four"
                    return "Full"
                case 4: 
                    return "Three"
                case 5:
                    return "One"
def evaluate_hand(hand, part2):
    data = {}
    cards = set()
    for h in hand:
        if not h in cards:
            data[h] = 0
            cards.add(h)
        data[h] += 1
    if part2 and "J" in cards:
        return evaluate_joker(data)
    length = len(data)
    match length:
        case 1:
            return "Five"
        case 2:
            for card, value in data.items():
                if value == 4:
                    return "Four"
            return "Full"
        case 3:
            for card, value in data.items():
                if value == 3:
                    return "Three"
                if value == 2:
                    return "Two"
        case 4:
            return "One"
        case 5:
            return "High"
def get_value(card):
    values = {
            "A":13,
            "K":12,
            "Q":11,
            "J":0,
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
    return values[card]
def compare(hand1, hand2):
    if get_value(hand1[0]) > get_value(hand2[0]):
        return False
    if get_value(hand1[0]) < get_value(hand2[0]):
        return True
    for i in range(5):
        if get_value(hand1[i]) > get_value(hand2[i]):
            return False
        if get_value(hand1[i]) < get_value(hand2[i]):
            return True
    
    
def part2():
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
    # input(evaluate_hand("9999J"))
    for line in lines:
        split_line = line.split(" ")
        hand = split_line[0]
        bet = split_line[1]
        evaluated_hand = evaluate_hand(hand,True)
        # print(evaluated_hand)
        # continue
        current_list = hands[evaluated_hand]
        # if current_list == []:
        #     current_list.append((hand, bet))
        #     continue
        index = 0
        found = False
        for index, item in enumerate(current_list):
            found = compare(hand, item[0])
            if found:
                break
        if found:    
            current_list.insert(index, (hand, bet))
        else:
            current_list.append((hand, bet))
        
    total_score = 0
    current_index = 0
    for hand_type in possible_hands:
        for card in hands[hand_type]:
            current_index += 1
            total_score += current_index * int(card[1])
            
            
    return total_score
def part1():
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
    # input(evaluate_hand("9999J"))
    for line in lines:
        split_line = line.split(" ")
        hand = split_line[0]
        bet = split_line[1]
        evaluated_hand = evaluate_hand(hand, False)
        # print(evaluated_hand)
        # continue
        current_list = hands[evaluated_hand]
        # if current_list == []:
        #     current_list.append((hand, bet))
        #     continue
        index = 0
        found = False
        for index, item in enumerate(current_list):
            found = compare(hand, item[0])
            if found:
                break
        if found:    
            current_list.insert(index, (hand, bet))
        else:
            current_list.append((hand, bet))
        
    total_score = 0
    current_index = 0
    for hand_type in possible_hands:
        for card in hands[hand_type]:
            current_index += 1
            total_score += current_index * int(card[1])
            
            
    return total_score
def solve():
    return (f"Part 1: {part1()}", f"Part 2: {part2()}")
        

        
