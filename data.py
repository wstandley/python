'''
    We are going to write a program that counts how many people order food, the cost of their order, add taxes, and a tip, then divide it by the number of people so they can split the check evenly.
'''

# variables

cost = 0
count = 3
tax_rate = .06
tip_percent = .25
total = 0

cost_1 = float(input("How much was the cost of the first order? ")) # Input lines
cost_2 = float(input("How much was the cost of the second order? "))
cost_3 = float(input("How much was the cost of the third order? "))

cost = cost_1 + cost_2 + cost_3 # Has to go before variable calcularions

tip_amt = cost * tip_percent
tax_amt = cost * tax_rate

total = tax_amt + tip_amt + cost

print(f"Your meal cost a total of: ${total: .2f} including taxes of ${tax_amt} and a {tip_percent}% tip that was ${tip_amt:.2f}")
print(f"You each owe ${total/3:.2f}")