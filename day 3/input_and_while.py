user = int(input('enter a number: '))

if user % 10 == 0:
    print("es multiplo")
else:
    print("no es multiplo ")
    
curren_number = 0

while curren_number <= 5:
    print(curren_number)
    curren_number += 1
    

promtp = 'tell me something and then i will repeat it back to you'
promtp += '\nEnter "quit" to finish que program.>> '
message = ''
while message != "quit":
    message = input(promtp)
    if message != "quit":
        print(message)
    