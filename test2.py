from dataclasses import dataclass, field
import random

@dataclass
class Bet:
    bet_numbers: list[int] = field(default_factory=list)
    bet_stars: list[int]  = field(default_factory=list)
    
    def set_bet_numbers(self, bet_numbers: list[int]):
        self.bet_numbers = bet_numbers

    def set_bet_stars(self, bet_stars: list[int]):
        self.bet_stars = bet_stars

@dataclass
class Ticket:
    bets: list[Bet] = field(default_factory=list) 
    


ticket=Ticket()

""" def generate_valid_numbers():
    numbers=[]
    while len(numbers) < 5:
        temp_bet = random.randint(1, 50)
        if temp_bet not in numbers:
            numbers.append(temp_bet)
    return numbers

def generate_valid_stars():
    stars=[]
    while len(stars) < 2:
        temp_star = random.randint(1, 12)
        if temp_star not in stars:
            stars.append(temp_star)
    return stars

for i in range(5):
    new_bet=Bet()

    new_bet.set_bet_numbers(generate_valid_numbers())

    new_bet.set_bet_stars(generate_valid_stars())

    ticket.bets.append(new_bet)

print(ticket) """


#def user_generate_valid_numbers(user_numbers):
#    user_num_list=+user_numbers
#    if not user_numbers.isdigit():
#        raise ValueError("Bet number must be an integer")
    
#    if user_numbers in user_num_list:
#        raise ValueError("Bet number already exists")
  
#    if int(user_numbers) < 1 or int(user_numbers) > 50:
#        raise ValueError("Bet number must be between 1 and 50")
  
    #user_num_list.append(user_numbers)
#    return user_num_list

def user_generate_valid_numbers(user_num_list):
    for x in user_num_list:
        if not x.isdigit():
            raise ValueError("Bet number must be an integer")
        if len(list(filter(lambda y: y==x, user_num_list))) > 1:
            raise ValueError("Bet number already exists")
        if int(x) < 1 or int(x) > 50:
            raise ValueError("Bet number must be between 1 and 50")
    return user_num_list

    #user_num_list=[]
    #mynewlist = "".join(str(s) for s in user_numbers)
    #print(type(mynewlist))
    
    #if not mynewlist.isdigit():
    #    raise ValueError("Bet number must be an integer")
    
    #if mynewlist in user_num_list:
    #    raise ValueError("Bet number already exists")#

    #if int(mynewlist) < 1 or int(mynewlist) > 12:
    #    raise ValueError("Bet number must be between 1 and 12")

    #temp_bet = random.randint(1, 50)
    #    if temp_bet not in numbers:
            #numbers.append(temp_bet)
    #eturn mynewlist


#def user_generate_valid_stars(user_stars):
    
    #if not user_stars.isdigit():
    #    raise ValueError("Bet star must be an integer")

    #if user_stars in user_stars_list:
    #    raise ValueError("Bet star already exists")#

    #if int(user_stars) < 1 or int(user_stars) > 12:
    #    raise ValueError("Bet star must be between 1 and 12")
    
    #user_stars_list.append(user_stars)
    
    #return int(stars)

def user_generate_valid_stars(user_stars_list):
    for x in user_stars_list:
        if not x.isdigit():
            raise ValueError("Bet star must be an integer")
        if len(list(filter(lambda y: y==x, user_stars_list))) > 1:
            raise ValueError("Bet star already exists")
        if int(x) < 1 or int(x) > 12:
            raise ValueError("Bet star must be between 1 and 12")
    return user_stars_list 




num_bets = int(input((f"Enter number of bets: ")))
new_bet = Bet()
for i in range(int(num_bets)):
    while True:
        print('i==',i)
        try:
            user_num_list = []
            while len(user_num_list) < 5:
                user_numbers = input(f"Enter Numbers {len(user_num_list) + 1}: ")
                user_num_list.append(user_numbers)

            user_stars_list = []
            while len(user_stars_list) < 2:
                user_stars = input((f"Enter Stars {len(user_stars_list) + 1}: "))
                user_stars_list.append(user_stars)
        
            
            new_bet.set_bet_numbers(user_generate_valid_numbers(user_num_list))
            new_bet.set_bet_stars(user_generate_valid_stars(user_stars_list))
            break
        except ValueError as e:
            print(e)
    ticket.bets.append(new_bet)

