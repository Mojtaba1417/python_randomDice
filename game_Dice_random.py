import random as rn

dice_one = [1,2,3,4,5,6]
dice_two = [1,2,3,4,5,6]

def shuffle_dice():
    for i in range(3):
        rn.shuffle(dice_one)
        rn.shuffle(dice_two)
    first_number = rn.choice(dice_one)
    second_number = rn.choice(dice_two)
    return first_number + second_number

def game():
    player_one_turn = rn.randint(1,100)
    player_two_turn = rn.randint(1,100)

    if player_one_turn > player_two_turn:
        player_one_score = shuffle_dice()
        player_two_score = shuffle_dice()

    else:
        player_two_score = shuffle_dice()
        player_one_score = shuffle_dice()

    if player_one_score > player_two_score:
        print(f' player one won with {player_one_score} score')
    else:
        print(f' player two won with {player_two_score} score')


game()

