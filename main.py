import day3.day3 as day3
import time as t

time = t.time()

solution = day3.solve()


with open("output.txt","w") as file:
    file.write(str(solution))
    
print("Success")

runtime = t.time() - time
print(runtime)