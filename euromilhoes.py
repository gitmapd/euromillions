from dataclasses import dataclass, field
import random
from num2words import num2words 
import os
import rich
from rich import table, prompt
import time
from rich.progress import track
from rich.console import Console
import sys
import time


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

menu_principal ={1: ['Boletim Automático', 'Automático'],
                 2: ['Boletim Manual', 'Manual'],
                 3: ['Ver premios','Premios'],
                 4: ['Sair', 'Saída'],
                 5: ['Win',"Win"]
                }

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

@dataclass
class Game:
    winning_numbers: list = field(default_factory=list)
    winning_stars: list = field(default_factory=list)
    
    def set_winning_numbers(self, winning_numbers: list):
        self.winning_numbers = winning_numbers

    def set_winning_stars(self, winning_stars: list):
        self.winning_stars = winning_stars

    def generate_winning_bet(self):
        self.set_winning_numbers(generate_valid_numbers())
        self.set_winning_stars(generate_valid_stars())

@dataclass
class Bet:
    bet_numbers: list = field(default_factory=list)
    bet_stars: list = field(default_factory=list)
    
    def set_bet_numbers(self, bet_numbers: list):
        self.bet_numbers = bet_numbers

    def set_bet_stars(self, bet_stars: list):
        self.bet_stars = bet_stars



@dataclass
class Ticket:
    bets: list = field(default_factory=list)


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


premios = {
    (5, 2): {"nome": "1º prémio"},
    (5, 1): {"nome": "2º prémio"},
    (5, 0): {"nome": "3º prémio"},
    (4, 2): {"nome": "4º prémio"},
    (4, 1): {"nome": "5º prémio"},
    (3, 2): {"nome": "6º prémio"},
    (4, 0): {"nome": "7º prémio"},
    (2, 2): {"nome": "8º prémio"},
    (3, 1): {"nome": "9º prémio"},
    (3, 0): {"nome": "10º prémio"},
    (1, 2): {"nome": "11º prémio"},
    (2, 1): {"nome": "12º prémio"},
    (2, 0): {"nome": "13º prémio"},
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

def check_bet_prize(bet, game):
    winning_numbers = game.winning_numbers
    winning_stars = game.winning_stars
    bet_numbers = bet.bet_numbers
    bet_stars = bet.bet_stars
    result1 = set(bet_numbers) & set(winning_numbers)
    result2 = set(bet_stars) & set(winning_stars)
    result1_len = len(result1)
    result2_len = len(result2)
    if (result1_len, result2_len) in premios:
        p = premios[(result1_len, result2_len)]
        return p['nome']
    return "Não há prémio"



def show_prizes(ticket, game):
    for bet in ticket.bets:
        p = check_bet_prize(bet, game)
        if p:
            return p

def main():
    ticket = Ticket()
    game = Game()
    game.generate_winning_bet()

    while True:
        print_menu(menu_principal)
        option = int(MyPrompt.ask("Selecione uma Opção", 
                 choices=[str(key) for key in menu_principal.keys()]))
        if option == 1:
            clear_screen()
            if MyConfirm.ask("Quer gerar um boletim automatico?", default=True):
                number_of_bets = int(MyPrompt.ask("Quantas apostas?", choices=[str(i) for i in range(1, 6)]))
                for _ in range(number_of_bets):
                        new_bet=Bet()
                        new_bet.set_bet_numbers(generate_valid_numbers())
                        new_bet.set_bet_stars(generate_valid_stars())
                        ticket.bets.append(new_bet)
             
                bets_table = table.Table(show_header=True, header_style="bold magenta", expand=True, highlight=True)
                bets_table.add_column("Apostas", justify="center")
                bets_table.add_column("Números", justify="center")
                bets_table.add_column("Estrelas", justify="left")

                for i in track(range(int(number_of_bets)), description="A Processar..."):
                    time.sleep(1)
                    bet = ticket.bets[i]
                    tickets_numbers = '  '.join(str(x).ljust(3) for x in bet.bet_numbers)
                    tickets_stars = '  '.join(str(x).ljust(3) for x in bet.bet_stars)
                    bets_table.add_row('Aposta '+str(i + 1),tickets_numbers, tickets_stars)
                
                console.rule("Boletim", style="bold yellow")
                console.print(bets_table)
                console.line()
                time.sleep(5)          
        if option == 2:
            clear_screen()
            ticket = Ticket()
            new_bet = Bet()
            if MyConfirm.ask("Quer gerar um boletim manual?", default=True):
                number_of_bets = int(MyPrompt.ask("Quantas apostas?", choices=[str(i) for i in range(1, 6)]))
                for i in range(int(number_of_bets)):
                        user_num_list = []
                        while len(user_num_list) < 5:
                            
                            user_number = MyPrompt.ask(f'Introduza os Números, o {num2words(len(user_num_list)+1,lang="pt",to="ordinal_num")}')
                            try:
                                user_generate_valid_numbers(user_num_list + [user_number])
                            except Exception as e:
                                console.print(e, style="bold red")
                            else:
                                user_num_list.append(user_number)
                        user_num_list = list(map(lambda x: int(x),user_num_list))
                        user_stars_list = []
                        while len(user_stars_list) < 2:
                            user_star = MyPrompt.ask(f'Introduza as Estrelas, o {num2words(len(user_stars_list) + 1,lang="pt",to="ordinal_num")}')
                            try:
                                user_generate_valid_stars(user_stars_list + [user_star])
                            except Exception as e:
                                console.print(e, style="bold red")
                            else:
                                user_stars_list.append(user_star)
                        user_stars_list = list(map(lambda x: int(x),user_stars_list)) 
                        new_bet.set_bet_numbers(user_num_list)
                        new_bet.set_bet_stars(user_stars_list)
                        
                        ticket.bets.append(new_bet)
                bets_table = table.Table(
                show_header=True, header_style="bold magenta", expand=True, highlight=True)
                bets_table.add_column("Apostas", justify="center")
                bets_table.add_column("Números", justify="center")
                bets_table.add_column("Estrelas", justify="left")

                for i in track(range(int(number_of_bets)), description="A Processar..."):
                    time.sleep(1) 
                    bet = ticket.bets[i]
                    tickets_numbers = '  '.join(str(x).ljust(3) for x in bet.bet_numbers)
                    tickets_stars = '  '.join(str(x).ljust(3) for x in bet.bet_stars)
                    bets_table.add_row('Aposta '+str(i + 1), tickets_numbers, tickets_stars)
                    console.rule("Boletim", style="bold yellow")
                    console.print(bets_table)
                    console.line()
                time.sleep(5)

        if option == 3:
            clear_screen()
            if MyConfirm.ask("Quer ver os seus prémios?", default=True):
                bets_table = table.Table(show_header=True, header_style="bold magenta", expand=True, highlight=True)
                bets_table.add_column("Apostas", justify="center")
                bets_table.add_column("Numeros", justify="left")
                bets_table.add_column("Estrelas", justify="left")
                bets_table.add_column("Premios", justify="left")
                bets_table.add_column("Chave", justify="left") 
                bets_table.add_column("Vencedora", justify="left")
                game_numbers = '  '.join(('[green]' + str(x) + '[/green]').ljust(3) if x in game.winning_numbers else str(x).ljust(3) for x in game.winning_numbers)
                game_stars = '  '.join(('[yellow]'+ str(x) + '[/yellow]').ljust(3) if x in game.winning_stars else str(x).ljust(3) for x in game.winning_stars)
                num_bets = range(int(len(ticket.bets)))
                for i in track(num_bets, description="A Processar..."):
                    time.sleep(1)
                    bet = ticket.bets[i]
                    tickets_numbers = '  '.join(('[green]' + str(x).ljust(3) + '[/green]') if x in game.winning_numbers else str(x).ljust(3) for x in bet.bet_numbers)
                    tickets_stars = '  '.join(('[yellow]'+ str(x).ljust(3) + '[/yellow]') if x in game.winning_stars else str(x).ljust(3) for x in bet.bet_stars)
                    bets_table.add_row(
                        'Aposta '+str(i+1),
                        tickets_numbers,
                        tickets_stars,
                        str(check_bet_prize(bet, game)),
                        game_numbers if i == 0 else "",
                        game_stars if i == 0 else ""
                   	)
                
                
                console.rule("Boletim", style="bold yellow")
                console.print(bets_table)
                console.line()
                time.sleep(5)
        if option == 4:
            clear_screen()
            console.print("Obrigado por ter jogado",style="bold red")
            sys.exit()
        
        if option == 5:
            winning_bet = Bet()
            winning_bet.set_bet_numbers(game.winning_numbers)
            winning_bet.set_bet_stars(game.winning_stars)
            ticket.bets.append(winning_bet)
            print(winning_bet)
            

if __name__ == '__main__':
	main()

