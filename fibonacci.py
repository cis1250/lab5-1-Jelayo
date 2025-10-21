#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def ask_input():
  fib = input("How many terms of the Fibonacci sequence would you like?")
  if int(fib) <= 0:
    while (fib <= 0):
      print("Pick a number greater than 0")
      input("How many terms of the Fibonacci sequence would you like?")
  else:
      x = 0
      y = 1
      z = 0
      print("0")
      for z in range (int(fib)):
          x, y = y, x + y
          if x >= int(fib): break
          fib_list = [x]      

def return_fibonacci():
  return fib_list
