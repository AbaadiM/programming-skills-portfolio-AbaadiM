sandwich_orders = ['beef', 'chicken', 'tuna', 'nutella']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()                                                      
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)                                                  

for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich.")