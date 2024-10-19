# Card validator with Luhn algorithm.

def cardValidator(func):
    def wrapper(card_number):
        if (card_number):
            try:
                card_list = list(card_number)
                check_digit = card_list.pop()
                card_list.reverse()

                processed_digits = []

                for index, digit in enumerate(card_list):
                    if index % 2 == 0:
                        control_digit = int(digit) * 2

                        if control_digit > 9:
                            control_digit = control_digit - 9
                        processed_digits.append(control_digit)
                    else:
                        processed_digits.append(int(digit))

                total_sum = int(check_digit) + sum(processed_digits)

                func('Valid!') if total_sum % 10 == 0 else func('Invalid')
            except ValueError:
                print('Value failure.')
            except TypeError:
                print('Type failure.')
        else:
            print('Card are not given. Try again.')
    return wrapper

@cardValidator
def validatorResponce(reponce):
    print(f'Yor card is: {reponce}')

validatorResponce(input('Please enter your card number: ').strip())