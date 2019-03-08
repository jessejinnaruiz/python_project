

print('\n~~~ Welcome to your terminal checkbook! ~~~\n')

print('What would you like to do? \n')


user_decision = input('''1) View current balance
2) Record a debit (withdraw)
3) Record a credit (deposit)
4) Exit\n''')


while not user_decision.isdigit() or int(user_decision) > 5 or input(user_decision) < 1:
    print(user_decision + ' is not a valid option. Please pick a valid number.\n')
    user_decision = input('''1) View current balance
2) Record a debit (withdraw)
3) Record a credit (deposit)
4) Exit\n''')
    continue
print(user_decision)