import argparse
import random

roll_template = """Rolls: {} Total: {} Average: {}"""

parser = argparse.ArgumentParser(description="Dice app")

parser.add_argument(
    'dice',
    help="A representation of the dice you want to roll"
)

parser.add_argument(
    '-r',
    '--repead',
    default=1,
    metavar='number',
    type=int,
    help="How many times to roll the specifed set of dice."
)

parser.add_argument(
    '-l',
    '--log',
    metavar='file',
    type=str,
    default='files/dice-roller-output.txt',
    help="Output to .txt?"
)

args = parser.parse_args()
dice_argument = args.dice
file_argument = args.log
repead_argument = args.repead

def format_dice(dice):
    try:
        quantity, die_size = [int(dice_p) for dice_p in dice.split('d')]
    except ValueError:
        raise ValueError('Invalid dice formatt.') from None
    else:
        return quantity, die_size
    

quantity, die_size = format_dice(dice_argument)

for _ in range(int(repead_argument)):
    rolls = [random.randint(1, die_size) for _ in range(quantity)]
    total = sum(rolls)
    avatrage = total / len(rolls)

def format_dice(rolls, total, avarage):
    rolls = ', '.join(str(role) for role in rolls)
    formatted_text = roll_template.format(rolls, total, avarage)
    return formatted_text

def log_output(rolls, total, avarage):
    try:
        with open(file_argument, 'a') as file:
            file.write(format_dice(rolls, total, avarage) + '\n')
            file.write('-' * 30 + '\n')
    except (FileExistsError, FileNotFoundError):
        raise OSError('File error') from None


log_output(rolls, total, avatrage)



