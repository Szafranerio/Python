print('Welcome to the calculator!')


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Error"
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    calculator_cont = True
    n1 = float(input("What is first number?: "))

    while calculator_cont:
        for symbol in operations:
            print(symbol)
        operation_symbol = input(
            'Pick an operation, + for sum, - for subtract, * for multiply, / for divide: ')
        n2 = float(input('What is second number?: '))
        answer = operations[operation_symbol](n1, n2)
        print(f'{n1} {operation_symbol} {n2} = {answer}')

        choice = input(
            'Do you want to use last result?: y for Yes, n for No?\n').lower()
        if choice == "y":
            n1 = answer
        else:
            calculator_cont = False
            print('\n' * 20)


calculator()
