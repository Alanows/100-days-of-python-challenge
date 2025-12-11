filename1 = 'gato.txt'
filename2 = 'perroo.txt'

#i show to the user what was the problem
try:
    with open(filename2,'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    print("that file doesn't exists")
else:
    for line in lines:
        print(line.strip())
        
    
    
#invisible error   
try:
    with open(filename1,'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    pass
else:
    for line in lines:
        print(line.strip())