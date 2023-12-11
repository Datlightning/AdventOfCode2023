from math import comb

pascals_triangle = {
    
}
def get_pascals_triangle(row):
    terms = []
    start = []
    end = []
    odd = row % 2 == 1
    if odd:
        for i in range(row//2 + 1):
            start.append(comb(row, i))
            end = [comb(row, i)] + end
        
    else:
        for i in range(row//2 + 1):
            start.append(comb(row, i))
            end= [comb(row, i)] + end
        del end[0]
    terms = start + end 
    return terms

def interpolate(numbers):
    steps = {
        0: numbers
    }
    factors = [0]
    current_step = 0
    while len(set(steps[current_step])) != 1:
        temp_numbers = []
        for i, value in enumerate(steps[current_step][:-1], start = 1):
            temp_numbers.append(steps[current_step][i] - value)
        current_step += 1
        factors.append(0)
        steps[current_step] = temp_numbers
        
    if current_step <= 1:
        return [steps[1][0], steps[0][0]]
    
    linear_term = steps[current_step-1][1] - steps[current_step-1][0]
    temp_factors = [linear_term, steps[current_step-1][0]]
    polynomial_level = 2
    current_step -= 1
   
    while current_step > 0:
        current_factors = []
        length = len(temp_factors)
        constant_term = steps[current_step-1][0]
        while temp_factors != []:
            coefficient = temp_factors[0]
            power = length 
            pascals_coefficients = []
            
            try:
                pascals_coefficients = pascals_triangle[power]
            except:
                pascals_coefficients = get_pascals_triangle(power)
                pascals_triangle[power] = pascals_coefficients
            current_factor = coefficient/pascals_coefficients[1]
            current_factors.append(current_factor)
            for i, term in enumerate(pascals_coefficients[2:], start=1):
                temp_factors[i] -= term * current_factor
            length -= 1
            del temp_factors[0]
            
        temp_factors = []
        temp_factors.extend(current_factors)
        temp_factors.append(constant_term)
        


        
        current_step -= 1
        polynomial_level += 1
    return temp_factors
def evaluate(func, x):
    output = 0 
 
    power = len(func) - 1
    
    for index, value in enumerate(func):
        output += x**(power - index) * value
    return output

    
    
def solve():
    lines=  []
    with open("day9/day9.txt", "r") as file:
        lines = file.read().strip().split("\n")
    part1 = 0
    part2 = 0
    for line in lines:
        numbers = list(map(int, line.split(" ")))
        
        function = interpolate(numbers)
        
        x = len(numbers)
        temp_score = evaluate(function, x)
        part1 += temp_score
        
        x = -1
        temp_score = evaluate(function, x)
        part2 += temp_score
        
    return f"Part 1: {int(part1)}\nPart 2: {int(part2)}"
