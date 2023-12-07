import day7.day7 as day7
import time as t

time = t.perf_counter()

solution = day7.solve()
print(solution)

with open("output.txt","w") as file:
    file.write(str(solution))
    
print("Success")

runtime = t.perf_counter() - time
print(f"{1000 * runtime} ms")