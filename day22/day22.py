
#shift all the bricks down
#find the bricks that are supported by atleast 2 other bricks
#find the bricks that are supported by 1 brick
#remove the bricks from the above set and return the length of the "2 supported" bricks.




class brick:
    def __init__(self, x1,y1,z1,x2,y2,z2,name):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
        self.name = name
        if x1 == x2 and y1 == y2 and z1 == z2:
            self.orientation = "a"
        elif x1 != x2:
            self.orientation = "x"
        elif y1 != y2:
            self.orientation = "y"
        elif z1 != z2:
            self.orientation = "z"
        self.supporting = set()
    def get_values(self):
        return (
            self.x1,
            self.y1,
            self.z1,
            self.x2,
            self.y2,
            self.z2
        )
    def add_support(self, brick):
        self.supporting.add(brick)
        return
    def is_intersection(self, brick):
        x1, y1, z1, x2, y2, z2 = brick.get_values()
        #not x1 x2 bx1 bx2
        x_range = not (max(self.x1, self.x2) < min(x1,x2) or max(x1,x2) < min(self.x1, self.x2)) 
        y_range = not (max(self.y1, self.y2) < min(y1,y2) or max(y1,y2) < min(self.y1, self.y2)) 
        z_range = not (max(self.z1, self.z2) < min(z1,z2) or max(z1,z2) < min(self.z1, self.z2)) 
        
        return x_range and y_range and z_range   
    def move_to(self, x):
            diff = self.z2 - self.z1
            self.z1 = x
            self.z2 = x + diff
           
    
    def to_string(self):
        return f"({self.x1},{self.y1},{self.z1}) to ({self.x2},{self.y2},{self.z2})"
    def equals(self, brick):
        return self.x1 == brick.x1 and self.y1 == brick.y1 and self.z1 == brick.z1 and self.x2 == brick.x2 and self.y2 == brick.y2 and self.z2 == brick.z2
    def overlap(self, brick):
        x1, y1, _, x2, y2, _ = brick.get_values()
        x_range = not (max(self.x1, self.x2) < min(x1,x2) or max(x1,x2) < min(self.x1, self.x2)) 
        y_range = not (max(self.y1, self.y2) < min(y1,y2) or max(y1,y2) < min(self.y1, self.y2)) 
        
        return x_range and y_range   
    
    def get_z(self):
        return max(self.z1, self.z2)
    def get_min_z(self):
        return min(self.z1, self.z2)
def collapsed(id, supporting, supported_by):
    # print(f"Id: {id}, Supporting: {supporting[id]}")
    if id not in supporting:
        return set()
    total = set()
    dependencies = {id}
    queue = [id]
    while queue:
        i = queue.pop(0)
        if i not in supporting:
            continue
        for ids in supporting[i]:
            if len(supported_by[ids].difference(dependencies)) == 0:
                total.add(ids)
                dependencies.add(ids)
                queue.append(ids)
    # print(total)
    return total
def solve():
    part1 = 0 
    part2 = 0
    bricks = []
    with open("day22/day22.txt", "r") as file:  
        for index, line in enumerate(file.read().strip().split("\n"), start = 1):
            split_line = line.split("~")
            c1 = eval("[" + split_line[0] + "]")
            c2 = eval("[" + split_line[1] + "]")
            new_brick = brick(c1[0],c1[1],c1[2],c2[0],c2[1],c2[2], index)
            
            
            bricks.append(new_brick)
    
    bricks.sort(key=lambda x: min(x.z1, x.z2))

    for b1 in bricks:
        closest_z = 1
        for b2 in bricks:
            if b1.name == b2.name:
                continue
            if not b2.overlap(b1):
                continue
            if b2.get_z() < b1.get_min_z():
                    closest_z = max(b2.get_z() + 1, closest_z)
            else:
                break       
        b1.move_to(closest_z)

                
                    
    bricks.sort(key=lambda x: min(x.z1, x.z2))
    
    supported_by = {}
    supporting = {}
    for index, below in enumerate(bricks):
        for n, above in enumerate(bricks[index+1:]):
            if above.overlap(below) and above.get_min_z() - 1 == below.get_z():
                if above.name in supported_by:
                    supported_by[above.name].add(below.name)
                else:
                    supported_by[above.name] = {below.name}
                if below.name in supporting:
                    supporting[below.name].add(above.name)
                else:
                    supporting[below.name] = {above.name}

    
        
    part1 = 0
    cant_delete = set()
    for value in supported_by.values():
        if len(value) == 1:
            cant_delete.update(value)
    # print(cant_delete)
    part1 = len(bricks) - len(cant_delete)
    
    part2 = 0
    for b in cant_delete:
        part2 += len(collapsed(b, supporting, supported_by))
        
    #114542 is too high
    return f"Part 1: {part1}\nPart 2: {part2}"

if __name__ == "__main__":
    print(solve())