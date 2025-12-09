print("welcome to division haha.")
print("insert two digit or 'q' if you wanna exit.")
while True:
    x = input("Inser the first digit --> ").lower()
    if x == 'q':
        break
    
    y = input("Inser the  second digit --> ").lower()
    if y == 'q':
        break
    
    try:
        answer =  int(x)/int(y)
    except:
        print("you can't divide by zero.")
    else:
        print(f"the answer is {answer}\n")
        print("let's try again with new two digits. (press enter:)")
        z = input("or press 'q' if you wanna close the program: ").lower()
        if z == 'q':
            break       