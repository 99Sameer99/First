import random


while True:
    player = input('Enter your name: ')
    print('Hello, ' + player)

    hand_choices = input()

    if len(hand_choices) == 0:
        inps = ['rock', 'paper', 'scissors']
    else:
        inps = hand_choices.split(',')

    file = open('rating.txt', 'r')
    player_list = dict()
    for lines in file:
        player_list[lines[0]] = lines[1]
    if player in player_list.keys():
        rating = player_list[player]
    else:
        rating = 0
    print('Okay, let\'s start')
    while True:
        move = inps[random.randint(0, len(inps)-1)]
        hand = input()
        if hand == '!exit':
            print('Bye! Your score: ', rating)
            break
        elif hand == '!rating':
            print(rating)
            continue
        elif hand not in inps:
            print('Invalid input')
            continue

        winning_hands = inps[(inps.index(hand))+1:]
        winning_hands.extend(inps[:inps.index(hand)])

        if hand == move:  # hand is users and move is of computers
            print('There is a draw (%s)' % move)
            rating += 50
        elif move in winning_hands[:(len(winning_hands)//2)] or move == winning_hands[0]:
            print('Sorry, but computer chose ', move)
        else:
            print('Well done. Computer chose %s and failed' % move)
            rating += 100
    break
