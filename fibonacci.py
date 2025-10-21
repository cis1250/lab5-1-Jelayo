def ask_input():
    fib = input("How many terms of the Fibonacci sequence would you like? ")
    if int(fib) <= 0:
        while (fib <= 0):
            print("Pick a number greater than 0")
            input("How many terms of the Fibonacci sequence would you like?")
    return fib

def return_fib(fib):
    x = 0
    y = 1
    z = 0
    fib_list = [0]
    for z in range (int(fib)):
        x, y = y, x + y
        if x >= int(fib): break
        fib_list.append(x)  
    return fib_list

def print_fib():
  fib = ask_input()
  fib_list = return_fib(fib)
  print(fib_list)

print_fib()
