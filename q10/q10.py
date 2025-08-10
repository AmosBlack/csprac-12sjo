#Q10

import pickle

n = int(input('enter no of customers: '))


with open("hotel.dat","ab") as f:

    for i in range(n):
        cust = eval(input("enter customer details: "))
        pickle.dump(cust, f)

with open("hotel.dat","rb") as f:
    customers = []
    while True:
        try:
            cust = pickle.load(f)
            customers.append(cust)
            print(cust)
        except EOFError:
            break
    
    print("the hotel has ", len(customers), "customers")
    print("the following customers have stayed for >2 days: ")
    for j in customers:
        if j['duration'] > 2:
            print(j['name'], end = " ")
    
'''
ojasmittal@pop-os ~/D/C/q10 (main)> python3 q10.py
enter no of customers: 3
enter customer details: {"roomno": 101, "name": "Amit", "duration": 3}
enter customer details: {"roomno": 105, "name": "Manish", "duration": 1}
enter customer details: {"roomno": 104, "name": "Pooja", "duration": 4}
the hotel has  3 customers
the following customers have stayed for >2 days: 
Amit Pooja 
ojasmittal@pop-os ~/D/C/q10 (main) [1]> python3 q10.py
enter no of customers: 1
enter customer details: {"roomno":301, "name":'Vidit', 'duration':3}  
{'roomno': 101, 'name': 'Amit', 'duration': 3}
{'roomno': 105, 'name': 'Manish', 'duration': 1}
{'roomno': 104, 'name': 'Pooja', 'duration': 4}
{'roomno': 301, 'name': 'Vidit', 'duration': 3}
the hotel has  4 customers
the following customers have stayed for >2 days: 
Amit Pooja Vidit 
'''