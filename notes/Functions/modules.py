#modules.py
#A Module is a file with a .py extension that contains code (usually functions)
#we want to use (import) in other python files/scripts 

#Before break we had a function for making pizzas:
def make_pizza(size, *toppings):
    """Summarize the pizza we want to make"""
    print(f"\nMaking a {size}-inch pizza with \
the following toppings: ")
    for topping in toppings:
        print(f"\t-{topping}")

def count_to_n(n):
    for number in range(1,n+1):
        print(number)