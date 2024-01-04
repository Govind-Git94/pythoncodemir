print("1.read\n2.write\n3.append")
cho = int(input("enter the number:-"))
container = ""
while True:
    if cho == 1:
        container = open("abc.txt",'r')
        read = container.read()
        print(read)
        break
    elif cho == 2:
        container = open("abc.txt", 'w')
        write = container.write(input("enter the data:-"))
        print(write)
        file = open("abc.txt", "r")
        print(file.read())
        break
    elif cho == 3:
        container = open("abc.txt", 'a')
        append = container.write(input("enter the data:-\n"))
        print(append)
        file = open("abc.txt", "r")
        print(file.read())
        break






