from dataclasses import dataclass, field
import random
import os
import rich
from rich import table, prompt
import time
from rich.progress import track
from rich.console import Console

class MyConfirm(prompt.Confirm):
    validate_error_message = "[prompt.invalid]Por favor introduzir S ou N"
    choices=['s','n']

class MyPrompt(prompt.PromptBase):
    validate_error_message = "[prompt.invalid]Por favor entra um valor válido"
    illegal_choice_message = (
        "[prompt.invalid.choice]Por favor seleciona uma das opções disponíveis"
    )
    prompt_suffix = ": "



MyConfirm = MyConfirm()
MyPrompt = MyPrompt()

console = Console()


def retorno_menu():
    menu_table = table.Table( show_header=True, header_style="bold magenta",
                                 title="Menu", expand=True, highlight=True
                                )
    menu_table.add_column("ID", justify="center")
    menu_table.add_column("Opções", justify="left")
    menu_table.add_column("Descrições", justify="left")
    for key, value in menu_retorno.items():
        menu_table.add_row(str(key), value[0], value[1])
    console.print(menu_table)

def principal_menu():
    
    menu_table = table.Table(show_header=True, header_style="bold magenta", title="Menu",expand=True,highlight=True)
    menu_table.add_column("ID", justify="center")
    menu_table.add_column("Opções", justify="left")
    menu_table.add_column("Descrições", justify="left")
    for key, value in menu_principal.items():
        menu_table.add_row(str(key), value[0],value[1] )
    console.print(menu_table)

def tickets_menu():
    menu_table = table.Table(show_header=True, header_style="bold magenta", title="Menu",expand=True,highlight=True)
    menu_table.add_column("ID", justify="center")
    menu_table.add_column("Opções", justify="left")
    menu_table.add_column("Descrições", justify="left")
    for key, value in menu_tickets.items():
        menu_table.add_row(str(key), value[0],value[1] )
    console.print(menu_table)



menu_principal ={1: ['Criar Tickets', 'Um ou mais Tickets'],
                 2: ['Sair', 'Sair do Programa']
                }
menu_tickets =  {1: ['Criar Apostas', 'Uma ou mais Apostas'],
                 2: ['Sair', 'Voltar ao inicio']
                }
menu_retorno =  {1: ['Menu Principal', 'Talões'],
                 2: ['Apostas', 'Menu Apostas'],
                 3: ['Sair', 'Sair do Programa']
                }


@dataclass
class Game:
    winning_numbers: list[int] = field(default_factory=list)
    winning_stars: list[int] = field(default_factory=list)
    
    def set_winning_numbers(self, winning_numbers: list[int]):
        self.winning_numbers = winning_numbers

    def set_winning_stars(self, winning_stars: list[int]):
        self.winning_stars = winning_stars



@dataclass
class Bet:
    bet_numbers: list[int] = field(default_factory=list)
    bet_stars: list[int] = field(default_factory=list)
    
    def set_bet_numbers(self, bet_numbers: list[int]):
        self.bet_numbers = bet_numbers

    def set_bet_stars(self, bet_stars: list[int]):
        self.bet_stars = bet_stars

def auto_generate_bet(self):
        self.bet_numbers, self.bet_stars = generate_valid_numbers()

def auto_generate_bet():
    numbers = []
    stars = []
    while len(numbers) < 5:
        temp_bet = random.randint(1, 50)
        if temp_bet not in numbers:
            numbers.append(temp_bet)
    while len(stars) < 2:
        temp_star = random.randint(1, 12)
        if temp_star not in stars:
            stars.append(temp_star)
    return numbers, stars


@dataclass
class Ticket:
    bets: list[Bet] = field(default_factory=list)


def generate_valid_numbers():
    numbers = []
    while len(numbers) < 5:
        temp_bet = random.randint(1, 50)
        if temp_bet not in numbers:
            numbers.append(temp_bet)
    return numbers

def generate_valid_stars():
    stars = []
    while len(stars) < 2:
        temp_star = random.randint(1, 12)
        if temp_star not in stars:
            stars.append(temp_star)
    return stars


prizes = {
    (5, 2): {"label": "1st prize"},
    (5, 1): {"label": "2nd prize"},
    (5, 0): {"label": "3rd prize"},
    (4, 2): {"label": "4rd prize"},
    (4, 1): {"label": "5th prize"},
    (3, 2): {"label": "6th prize"},
    (4, 0): {"label": "7th prize"},
    (2, 2): {"label": "8th prize"},
    (3, 1): {"label": "9th prize"},
    (3, 0): {"label": "10th prize"},
    (1, 2): {"label": "11th prize"},
    (2, 1): {"label": "12th prize"},
    (2, 0): {"label": "13th prize"},
}


def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def user_generate_valid_numbers(user_num_list):
    for x in user_num_list:
        if not x.isdigit():
            raise ValueError("Número não é um dígito")
        if len(list(filter(lambda y: y==x, user_num_list))) > 1:
            raise ValueError("Número já existe")
        if int(x) < 1 or int(x) > 50:
            raise ValueError("Número deve estar entre 1 e 50")
    return user_num_list

def user_generate_valid_stars(user_stars_list):
    for x in user_stars_list:
        if not x.isdigit():
            raise ValueError("Estrela não é um dígito")
        if len(list(filter(lambda y: y==x, user_stars_list))) > 1:
            raise ValueError("Estrela já existe")
        if int(x) < 1 or int(x) > 12:
            raise ValueError("Estrela tem de ser entre 1 e 12")
    return user_stars_list 

# A prize consists how many numbers and stars are common to the
# Game winning key.(5,2) -> "1st prize", that means all numbers and stars
# are in a winning bet.
# A Ticket can consist of 1 to multiple winning bets.


def check_if_user_won(ticket, game):
    winning_numbers = game.winning_numbers
    winning_stars = game.winning_stars
    bet_numbers = 0
    bet_stars = 0
    for index, bet in enumerate(ticket.bets):
        bet_numbers = bet.bet_numbers
        bet_stars = bet.bet_stars
        result1 = set(bet_numbers) & set(winning_numbers)
        result2 = set(bet_stars) & set(winning_stars)
        result1_len = len(result1)
        result2_len = len(result2)
        if (result1_len, result2_len) in prizes:
            p = prizes[(result1_len, result2_len)]
            return (f'{p[0]}{p["label"]}')
        else:
            return (f"YOU LOST!")


def play_game():
    game = Game()
    
    game.set_winning_numbers(generate_valid_numbers())

    game.set_winning_stars(generate_valid_stars())
    
    tickets_menu()
    while True:
        option = int(MyPrompt.ask("Select an option", choices=[
                     str(key) for key in menu_tickets.keys()]))
        if option == 1:
            ticket = Ticket()
            if MyConfirm.ask("Do you want to auto-generate a random ticket?", default=True):
                num_bets = MyPrompt.ask(f"Enter number of bets")
                for _ in range(int(num_bets)):
                    new_bet = Bet()
                    new_bet.auto_generate_bet()
                    ticket.bets.append(new_bet)

                bets_table = table.Table(show_header=True, header_style="bold magenta", expand=True, highlight=True)
                bets_table.add_column("Apostas", justify="center")
                bets_table.add_column("Números", justify="center")
                bets_table.add_column("Estrelas", justify="left")

                for i in track(range(int(num_bets)), description="A Processar..."):
                    time.sleep(1)
                    tickets_numbers = '  '.join(str(x).ljust(3) for x in ticket.bets[i].bet_numbers)
                    tickets_stars = '  '.join(str(x).ljust(3) for x in ticket.bets[i].bet_stars)
                    bets_table.add_row('Aposta '+str(i + 1),tickets_numbers, tickets_stars)
                clear_screen()
                console.rule("Boletim", style="bold yellow")
                console.print(bets_table)
                console.line()
        if option == 2:
            ticket = Ticket()
            new_bet = Bet()
            if MyConfirm.ask("Do you want to to generate a manual ticket?", default=True):
                num_bets = MyPrompt.ask(f"Enter number of bets")
                for i in range(int(num_bets)):
                    while True:
                        try:
                            user_num_list = []
                            while len(user_num_list) < 5:
                                user_numbers = MyPrompt.ask(f"Enter Numbers {len(user_num_list) + 1}: ")
                                user_num_list.append(user_numbers)
                            
                            user_stars_list = []
                            while len(user_stars_list) < 2:
                                user_stars = MyPrompt.ask(f"Enter Stars {len(user_stars_list) + 1}")
                                user_stars_list.append(user_stars)
                            
                            new_bet.set_bet_numbers(user_generate_valid_numbers(user_num_list))
                            new_bet.set_bet_stars(user_generate_valid_stars(user_stars_list))
                            break
                        except ValueError as e:
                            print("Aposta Errada",e)
                    ticket.bets.append(new_bet)

                bets_table = table.Table(
                show_header=True, header_style="bold magenta", expand=True, highlight=True)
                bets_table.add_column("Apostas", justify="center")
                bets_table.add_column("Números", justify="center")
                bets_table.add_column("Estrelas", justify="left")

                for i in track(range(int(num_bets)), description="A Processar..."):
                    time.sleep(1)
                    tickets_numbers = '  '.join(str(x).ljust(3) for x in ticket.bets[i].bet_numbers)
                    tickets_stars = '  '.join(str(x).ljust(3) for x in ticket.bets[i].bet_stars)
                    bets_table.add_row('Aposta '+str(i + 1), tickets_numbers, tickets_stars)
                    clear_screen()
                    console.rule("Boletim", style="bold yellow")
                    console.print(bets_table)
                    console.line()
        #time.sleep(5)
        #retorno_menu()
        option = int(MyPrompt.ask("Select an option", choices=[str(key) for key in menu_retorno.keys()]))
        if option == 1:
            principal_menu()
        elif option == 2:
            tickets_menu()
        elif option == 3:
            exit()

        # elif option == 2:
        #    return
        elif option == 2:
            # exit()
            console.print(check_if_user_won(ticket, game))


if __name__ == '__main__':
    while True:
        principal_menu()
        option = int(MyPrompt.ask("Select an option", choices=[
                     str(key) for key in menu_principal.keys()]))
        if option == 1:
            play_game()

        #        tickets=int(prompt.Prompt.ask("Select an option", choices=[str(key) for key in menu_tickets.keys()]))
        #        ticket=Ticket()
        #
        # elif option == 2:
            # console.print(game)
        elif option == 2:
            exit()

# bets=Bet()
# bets.winning_numbers()
# ticket=Ticket()
# ticket.Bets.append(bets)
# print(ticket.Bets)
