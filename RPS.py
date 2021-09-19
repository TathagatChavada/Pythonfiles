import random as r
print('\t1. Rock.\n'
      '\t2. Paper.\n'
      '\t3. Scissor.\n')


lst = ['Rock', 'Paper', 'Scissor']



while True:
    Your_choice = int(input('Enter your choice: '))

    if Your_choice == 1:
        Bot_choice = r.choice(lst)

        if Bot_choice == lst[0]:
            print(f'Your choice is {lst[0]} and choice of Bot is {Bot_choice} and Match tied....')

        elif Bot_choice == lst[1]:
            print(f'Your choice is {lst[0]} and choice of Bot is {Bot_choice} You Lose ☹️')

        elif Bot_choice == lst[2]:
            print(f'Your choice is {lst[0]} and choice of Bot is {Bot_choice} You Won 😃')

        else:
            pass

    elif Your_choice == 2:
        Bot_choice = r.choice(lst)

        if Bot_choice == lst[0]:
            print(f'Your choice is {lst[1]} and choice of Bot is {Bot_choice} You Won 😃')

        elif Bot_choice == lst[1]:
            print(f'Your choice is {lst[1]} and choice of Bot is {Bot_choice} Match tied....')

        elif Bot_choice == lst[2]:
            print(f'Your choice is {lst[1]} and choice of Bot is {Bot_choice} You Lose ☹️')

        else:
            pass

    elif Your_choice == 3:
        Bot_choice = r.choice(lst)
        
        if Bot_choice == lst[0]:
            print(f'Your choice is {lst[2]} and choice of Bot is {Bot_choice} You Lose ☹️')

        elif Bot_choice == lst[1]:
            print(f'Your choice is {lst[2]} and choice of Bot is {Bot_choice} You Won 😃')

        elif Bot_choice == lst[2]:
            print(f'Your choice is {lst[2]} and choice of Bot is {Bot_choice} Match tied...')

        else:
            pass

    else:
        print('Invalid choice!!!')

    ans = input('Do You want to play again (y or Y)?: ')
    if ans.lower() != 'y':
        break

    print('\n')