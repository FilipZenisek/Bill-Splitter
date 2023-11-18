# write your code here
import random
# Split whole value of the lucky one to other members.
# For example: Total bill value = 100
# Members = 5
# One of the member is the lucky one, so he will pay nothing.
# 100 / 4 = 25 for each member, expect for the one.


def checking_input():
    n_of_friends = int(input('Enter the number of friends joining (including you):\n'))
    return n_of_friends


def implementing_names_and_values(n_of_friends):
    dictionary = {}
    print('Enter the name of every friend (including you), each on a new line:')
    for _ in range(n_of_friends):
        name = input()
        dictionary[name] = 0

    total_bill = int(input('\nEnter the total bill value:\n'))

    for name in dictionary:
        dictionary[name] = round(total_bill / n_of_friends, 2)

    return dictionary, total_bill


def who_is_lucky(dictionary_with_names_and_values, bill, n_of_friends):
    decision = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if decision.lower() == 'yes':
        n_of_friends -= 1
        lucky_name = random.choice(list(dictionary_with_names_and_values))
        print(f'\n{lucky_name} is the lucky one!\n')
        # Changes value of bill to zero for the chosen lucky guy
        for name in dictionary_with_names_and_values:
            if name == lucky_name:
                dictionary_with_names_and_values[name] = 0
            else:
                dictionary_with_names_and_values[name] = round(bill / n_of_friends, 2)
    else:
        print('\nNo one is going to be lucky\n')

    return dictionary_with_names_and_values


def main():
    n_of_friends = checking_input()
    if n_of_friends > 0:
        dictionary_with_names_and_values, total_bill = implementing_names_and_values(n_of_friends)
        print(who_is_lucky(dictionary_with_names_and_values, total_bill, n_of_friends))
    else:
        print('No one is joining for the party')


if __name__ == '__main__':
    main()
