from dataclasses import dataclass, field
import random
import os
import rich
from rich import table, prompt
import time
from rich.progress import track
from rich.console import Console

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

def play_game():
    game = Game()
    
    game.set_winning_numbers(generate_valid_numbers())

    game.set_winning_stars(generate_valid_stars())

    print_menu(menu_principal)
    
play_game()