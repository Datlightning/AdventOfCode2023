import day1 
with open("output.txt","w") as file:
    data = day1.solve()
    file.write(data)