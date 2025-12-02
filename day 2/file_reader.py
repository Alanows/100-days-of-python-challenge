file_name = 'ejercisios cap 10/pi_10000_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()
        
text_line_file = ''
for line in lines:
    text_line_file += line.strip()
    
birthday_exits = input("Enter your birthday in this form ddmmyy: ")
if birthday_exits in text_line_file:
    print("yep your birthday is in the first million digit of PI number")
else:
    print('nop your birthday is not in the first million digit of pin number')
print(text_line_file[:52])
print(len(text_line_file))