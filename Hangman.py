import random

print('H A N G M A N\n')
words = ['python', 'java', 'kotlin', 'javascript', 'bootstrap', 'html', 'css', 'fullstack', 'crocodile', 'extinction']
while True:
    choice = input('Type "p" to play the game, "e" to quit:')
    if choice == 'e':
        break
    elif choice == 'p':
        print('\n')
        n = random.randint(0, len(words) - 1)
        tries = 1
        letterset = set()
        figured = '-' * len(words[n])
        while tries <= 8:
            print(figured)
            if figured == words[n]:
                break
            figured = ''
            letter = input('Input a letter: ')
            if len(letter) != 1:
                print('You should input a single letter')

            elif letter.isalpha() == False or letter.islower() == False:  # 'a' > letter > 'z':
                print('It is not an ASCII lowercase letter')

            elif letter not in set(words[n]):
                if letter in letterset:
                    print('You already typed this letter')
                else:
                    letterset.add(letter)
                    print('No such letter in the word')
                    tries += 1

            elif letter in set(words[n]):
                if letter in letterset:
                    print('You already typed this letter')
                else:
                    letterset.add(letter)

            if tries <= 8:
                print('\n')

            for i in words[n]:
                if i in letterset:
                    figured += i
                else:
                    figured += '-'

        if figured == words[n]:
            print('You survived!')
        else:
            print('You are hanged!')
