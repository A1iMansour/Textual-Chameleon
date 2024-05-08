def save_exp_number(exp_number):
    with open('exp_number.txt', 'w') as f:
        f.write(str(exp_number))

def load_exp_number():
    try:
        with open('exp_number.txt', 'r') as f:
            return int(f.read())
    except FileNotFoundError:
        return 1  # Default value


