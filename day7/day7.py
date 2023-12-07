import random as r
def evaluate_hand(hand):
    data = {}
    cards = set()
    for h in hand:
        if not h in cards:
            data[h] = 0
            cards.add(h)
        data[h] += 1
       
        if data[h] == 4 and len(data) == 2:
            return "Four"
    length = len(data)
    match length:
        case 1:
            return "Five"
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
        case 5:
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
    return values[card]
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
        evaluated_hand = evaluate_hand(hand)
        # print(evaluated_hand)
        # continue
        current_list = hands[evaluated_hand]
        # if current_list == []:
        #     current_list.append((hand, bet))
        #     continue
        index = 0
        found = False
        for index, item in enumerate(current_list):
            
            if get_value(hand[0]) < get_value(item[0][0]):
                found = True
                
                break
            if get_value(hand[0]) == get_value(item[0][0]):
                i = 0     
                           
                while i < 5:
                    if get_value(hand[i]) < get_value(item[0][i]):
                            found = True
                         
                            break
                    if  get_value(hand[i]) > get_value(item[0][i]):
                            index += 1
                            found = True
                            break
                    i+=1     
            if found:
                break
      
        if found:    
            current_list.insert(index, (hand, bet))
        else:
            current_list.append((hand, bet))
        # hands[evaluated_hand] = current_list
    total_score = 0
    current_index = 0
    for hand_type in possible_hands:
        for card in hands[hand_type]:
            current_index += 1
            total_score += current_index * int(card[1])
    return total_score
#249517775
#249570620
#249593835


#249390788
print(solve())
        

        
