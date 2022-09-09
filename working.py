from dataclasses import dataclass, field
import random
import os
import rich
from rich import table, prompt
import time
from rich.progress import track
from rich.console import Console
import sys

console = Console()

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
menu_automatico_manual = {1: ['Criar Boletins Automáticos', 'Um ou mais Tickets'],
                          2: ['Criar boletins manuais', 'Sair do Programa'],
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

@dataclass
class Ticket:
    bets: list[Bet] = field(default_factory=list)



def print_menu(menu):
    menu_table = table.Table( show_header=True, header_style="bold magenta",
                                 title="Menu", expand=True, highlight=True
                                )
    menu_table.add_column("ID", justify="center")
    menu_table.add_column("Opções", justify="left")
    menu_table.add_column("Descrições", justify="left")
    for key, value in menu.items():
        menu_table.add_row(str(key), value[0], value[1])
    console.print(menu_table)

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

def create_auto_tickets():
    new_bet=Bet()
    ticket=Ticket()
    num_tickets = 0
    while not num_tickets in range(1,6):
        num_tickets = int(MyPrompt.ask(f"Introduza o número de boletins"))
    print_menu(menu_automatico_manual)
    option = int(MyPrompt.ask("Select an option", choices=[str(key) for key in menu_automatico_manual.keys()]))
    if option == 1:
        if MyConfirm.ask("Do you want to auto-generate a random ticket?", default=True):
            for _ in range(num_tickets):
                num_bets = MyPrompt.ask(f"Enter number of bets")
                for _ in range(int(num_bets)):
                    new_bet.set_bet_numbers(generate_valid_numbers())
                    new_bet.set_bet_stars(generate_valid_stars())
                    ticket.bets.append(new_bet)

def create_manual_tickets():
    new_bet=Bet()
    ticket=Ticket()
    num_tickets = 0
    while not num_tickets in range(1,6):
        num_tickets = int(MyPrompt.ask(f"Introduza o número de boletins"))
    print_menu(menu_automatico_manual)
    if MyConfirm.ask("Do you want to to generate a manual ticket?", default=True):
        num_bets = MyPrompt.ask(f"Enter number of bets")
        for i in range(int(num_bets)):
            user_num_list = []
            while len(user_num_list) < 5:
                user_number = MyPrompt.ask(f"Enter Numbers {len(user_num_list) + 1}: ")
            try:
                user_generate_valid_numbers(user_num_list + [user_number])
            except Exception as e:
                print(e)
            else:
                user_num_list.append(user_number)

            user_stars_list = []
            while len(user_stars_list) < 2:
                user_star = MyPrompt.ask(f"Enter Stars {len(user_stars_list) + 1}")
                try:
                    user_generate_valid_stars(user_stars_list + [user_star])
                except Exception as e:
                    print(e)
                else:
                    user_stars_list.append(user_star)
                            
                new_bet.set_bet_numbers(user_num_list)
                new_bet.set_bet_stars(user_stars_list)
            ticket.bets.append(new_bet)

def play_game():
    game = Game()
    
    game.set_winning_numbers(generate_valid_numbers())

    game.set_winning_stars(generate_valid_stars())

    while True:
        print_menu(menu_principal)
        option = int(MyPrompt.ask("Selecionar opção", choices=[
            str(key) for key in menu_principal.keys()]))
        if option == 1:
            create_auto_tickets()
        if option == 2:
            create_manual_tickets()
                
        
        if option == 3:
            sys.exit()            

play_game()