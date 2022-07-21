def add(*Numbers):
    Solution = 0
    Length = len(Numbers)
    print(Length)
    for i in range(0,len(Numbers)):
        Solution = Solution + Numbers[i]
    print("The Solution of Sum is",Solution)

add(2,3)
add(4,6,7)

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Anusha", Lastname="Konderu", Age=32, Phone=9885678939)
intro(Firstname="Santhoshi", Lastname="Aravala", Email="sairam@gmail.com", Country="India", Age=35, Phone=7666652524)