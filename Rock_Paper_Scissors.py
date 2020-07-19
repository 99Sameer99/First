import random


while True:
    player = input('Enter your name(case sensitive): ')
    print('Hello, ' + player)

    print('Enter hands separated by \',\' \nor else just press enter to choose Rock-paper-scissors.')

    hand_choices = input('=>')

    if len(hand_choices) == 0:
        inps = ['rock', 'paper', 'scissors']
    else:
        inps = hand_choices.split(',')

    file = open('rating.txt', 'r+')

    player_list = dict()
    content = file.read()

    choice = input('Do you want to see saved data.\nif yes enter y or n for no:> ')
    if choice == 'y':
        print(content)

    for lines in content.split('\n')[:-1]:
        info = lines.rstrip('\n').split(' ')
        player_list[info[0]] = int(info[1])

    if player in player_list.keys():
        rating = player_list[player]
    else:
        rating = 0

    print('Okay, let\'s start\n')
    while True:
        move = inps[random.randint(0, len(inps)-1)]
        hand = input('=>')  # hand is users and move is of computers.

        if hand == '!exit':
            print('Bye! Your score: ', rating)
            player_list[player] = rating
            file.seek(0)
            file.truncate(0)
            for key, value in player_list.items():
                saving_info = key + ' ' + str(value) + '\n'
                file.write(saving_info)
            file.close()
            break

        elif hand == '!rating':
            print(rating)
            continue

        elif hand not in inps:
            print('Invalid input')
            continue

        winning_hands = inps[(inps.index(hand))+1:]
        winning_hands.extend(inps[:inps.index(hand)])

        if hand == move:
            print('There is a draw (%s)' % move)
            rating += 50

        elif move in winning_hands[:(len(winning_hands)//2)] or move == winning_hands[0]:
            print('Sorry, but computer chose ', move)

        else:
            print('Well done. Computer chose %s and failed' % move)
            rating += 100

    break

