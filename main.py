import day9.day9 as day9
import time as t

time = t.perf_counter()

solution = day9.solve()
print(solution)

with open("output.txt","w") as file:
    file.write(str(solution))
    
print("Success")

runtime = t.perf_counter() - time
print(f"{1000 * runtime} ms")