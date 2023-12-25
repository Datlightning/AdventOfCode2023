#(x-1) = 2(y-1)
#dx * x - dx * x1 = dy * y - dy * y1
#dx * x - dy * y  + dy * y1 - dx * x1 = 0
import sympy
def generate_line(x1,y1,dx,dy):

    y_side = -y1 * dx
    x_side = -x1 * dy
    constant_term = x_side - y_side
    x_coefficient = dy
    y_coefficient = -dx
    return [x_coefficient, y_coefficient, constant_term]
def solve():
    part1 = 0 
    part2 = 0
    point_slope = []
    point_slope_3D = []
    with open("day24/day24.txt", "r") as file:  
        for line in file.read().strip().split("\n"):
            split_line = "[" + line.replace("@",",") + "]"
            x,y,z,dx,dy,dz = eval(split_line)
            point_slope.append((x,y,dx,dy))
            point_slope_3D.append((x,y,z,dx,dy,dz))
    small = 200000000000000
    big = 400000000000000
    visited = set()
    for i,line1 in enumerate(point_slope_3D):
            # print(i)
        
            for j,line2 in enumerate(point_slope_3D):
                if (line1, line2) in visited or (line2, line1) in visited:
                    continue
                if line1 == line2:
                    continue
                visited.add((line1,line2))
                visited.add((line2,line1))


                x1,y1,dx1,dy1 = point_slope[i]
                x2,y2,dx2,dy2 = point_slope[j]

                a1,b1,c1 = generate_line(x1,y1,dx1,dy1)
                a2,b2,c2 = generate_line(x2,y2,dx2,dy2)

                den = (a1 * b2) - (a2 * b1)
                
                if den == 0:
                    continue
                intersection = (((b1*c2) - (b2*c1))/den, ((c1*a2)-(c2*a1))/den)
                ahead1 = (dx1  > 0) == (intersection[0] > x1)

                ahead2 = (dx2 > 0) == (intersection[0] > x2)
                if small<=intersection[0]<=big and small<=intersection[1]<=big and ahead1 and ahead2:
                    part1 += 1                    

        
    xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, dxr,dyr,dzr")
    equations = []
    for i,( sx, sy, sz, vx, vy, vz) in enumerate(point_slope_3D):
        equations.append((xr - sx) * (vy -  vyr) - (yr - sy) * (vx - vxr))
        equations.append((yr - sy) * (vz - vzr)  - (zr -sz) * (vy - vyr))
        if i < 2:
            continue

        answers = [soln for soln in sympy.solve(equations) if all(x % 1 == 0 for x in soln.values())]
        if len(answers) == 1:
            answer = answers
            break
    part2 = answer[0][xr] + answer[0][yr] + answer[0][zr]

    return f"Part 1: {part1}\nPart 2: {part2}"

if __name__ == "__main__":
    print(solve())