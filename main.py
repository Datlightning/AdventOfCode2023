import day4.day4 as day4
import time as t

time = t.perf_counter()

solution = day4.solve()


with open("output.txt","w") as file:
    file.write(str(solution))
    
print("Success")

runtime = t.perf_counter() - time
print(runtime)