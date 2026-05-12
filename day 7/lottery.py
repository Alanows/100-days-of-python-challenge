import random
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z']

number_for_lottery = list(range(100))
number_random_for_lottery = alphabet + number_for_lottery

class Lottery:
    def __init__(self,ticket):
        self.ticket = ticket
    
    def random_choices(self):
        the_winner_number = []
        for i in range(8):
            the_winner_number.append(random.choice(self.ticket))
        
        self.ticket = the_winner_number
    
    def my_ticket(self):
        trys = 0
        while True:
            my_ticket_number = []
            for i in range(8):
                my_ticket_number.append(random.choice(self.ticket))
            trys += 1
             
            if my_ticket_number == self.ticket:
                print('YOU WON!!!')
                print(f"we made a {trys} attemps")
                break   
          
    def winner_ticket(self):
        print(f"the winner ticket is: " ,*self.ticket)        
      
x = Lottery(number_random_for_lottery)

x.random_choices()
x.my_ticket()
x.winner_ticket()