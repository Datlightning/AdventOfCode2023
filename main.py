import day5.day5 as day5
import time as t

time = t.perf_counter()

solution = day5.solve()


with open("output.txt","w") as file:
    file.write(str(solution))
    
print("Success")

runtime = t.perf_counter() - time
print(runtime)