from sys import exit, argv

def decompose(number):
    billets = []
    for billet in tickets:
        while True:
            new_value = number - billet
            if new_value >= 0:
                billets.append(billet)
                number = new_value
            else:
                break
    return billets



tickets = [100, 50, 20, 10, 5, 2, 1]

price = argv[1]

try:
    float(price)
    price = eval(price)
    if isinstance(price, float):
        exit("argument must be integer, not float")
except ValueError:
    exit("argument must be integer!")

print(decompose(price))
