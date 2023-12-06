import day6.day6 as day6
import time as t

time = t.perf_counter()

solution = day6.solve()


with open("output.txt","w") as file:
    file.write(str(solution))
    
print("Success")

runtime = t.perf_counter() - time
print(f"{1000 * runtime} ms")