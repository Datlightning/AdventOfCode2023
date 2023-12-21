import day20.day20 as day
import time as t

time = t.perf_counter()

solution = day.solve()
print(solution)

with open("output.txt","w") as file:
    file.write(str(solution))
    
print("Success")

runtime = t.perf_counter() - time
print(f"{1000 * runtime} ms")