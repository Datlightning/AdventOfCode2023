import day2.day2 as day2
data = day2.solve()
 
with open("output.txt","w") as file:
    file.write(str(data))