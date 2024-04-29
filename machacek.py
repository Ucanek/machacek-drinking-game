from random import randint

def throw_dice():
    first_dice_throw = randint(1, 6)
    second_dice_throw = randint(1, 6)
    return first_dice_throw, second_dice_throw

def make_machacek_numbers():
    first_dice_throw, second_dice_throw = throw_dice()
    dice_value = 0

    if first_dice_throw == 2 and second_dice_throw == 1:
        dice_value = 21

    elif first_dice_throw == 1 and second_dice_throw == 2:
        dice_value = 21

    elif first_dice_throw > second_dice_throw:
        dice_value = (first_dice_throw * 10) + second_dice_throw

    elif second_dice_throw > first_dice_throw:
        dice_value = (second_dice_throw * 10) + first_dice_throw

    elif first_dice_throw == second_dice_throw:
        dice_value = (first_dice_throw * 100)

    return dice_value

def machacek_simulate(num_challenges, enable_output):
    value = 1
    fines = [0, 0, 0]
    seznam = []
    player_number = 1
    num_players = 3
    for i in range(num_challenges):
        dice_value = make_machacek_numbers()
        seznam.append(dice_value)
        next_player = (player_number % num_players) + 1
        next_player1 = next_player - 1

        if next_player1 == 0:
            next_player1 = 3

        if value == 1:
            value -= 1
            if enable_output:
                print(f'Hrac c. {player_number} hodil {seznam[i]} (nahazuje)')
                print(f'  Hrac c. {player_number} oznamuje hraci c. {next_player} hodnotu {seznam[i]}')
                print(f'    Hrac c. {next_player} akceptuje')

        elif seznam[i] == 21:
            if enable_output:
                print(f'Hrac c. {player_number} hodil {seznam[i]} (přehazuje {seznam[i-1]})')
                print(f'  Hrac c. {player_number} oznamuje hraci c. {next_player} hodnotu {seznam[i]}')
                print(f'    Hrac c. {next_player} akceptuje')

        elif seznam[i] > seznam[i-1] == 21:
            fines[player_number - 1] += 1
            value += 1
            if enable_output:
                print(f'Hrac c. {player_number} hodil {seznam[i]} (přehazuje {seznam[i-1]})')
                print(f'  Hrac c. {player_number} oznamuje hraci c. {next_player} hodnotu {seznam[i]}')
                print(f'    Hrac c. {next_player} hod rozporuje')
                print(f'      Hrac c. {next_player1} je usvedcen ze lzi a dostava pokutu.')

        elif seznam[i] <= seznam[i-1]:
            fines[player_number - 1] += 1
            value += 1
            if enable_output:
                print(f'Hrac c. {player_number} hodil {seznam[i]} (přehazuje {seznam[i-1]})')
                print(f'  Hrac c. {player_number} oznamuje hraci c. {next_player} hodnotu {seznam[i]}')
                print(f'    Hrac c. {next_player} hod rozporuje')
                print(f'      Hrac c. {next_player1} je usvedcen ze lzi a dostava pokutu.')

        elif seznam[i] == 21 >= seznam[i-1] == 21:
            if enable_output:
                print(f'Hrac c. {player_number} hodil {seznam[i]} (přehazuje {seznam[i-1]})')
                print(f'  Hrac c. {player_number} oznamuje hraci c. {next_player} hodnotu {seznam[i]}')
                print(f'    Hrac c. {next_player} akceptuje')

        else:
            if enable_output:
                print(f'Hrac c. {player_number} hodil {seznam[i]} (přehazuje {seznam[i-1]})')
                print(f'  Hrac c. {player_number} oznamuje hraci c. {next_player} hodnotu {seznam[i]}')
                print(f'    Hrac c. {next_player} akceptuje')

        player_number = (player_number % num_players) + 1

    if enable_output:
        print('Koncove skore:')
        for i, fine in enumerate(fines):
            print(f' Hrac c. {i + 1}: {fine} pokut')

    max_fines = max(fines)
    most_fined = fines.index(max_fines) + 1

    return fines

def machacek_stats(num_games, num_challenges):
    enable_output = False
    my_list_of_fines = [0, 0, 0]

    if num_games == 1:
        print(f'Simulovana {num_games} hra')
    elif num_games in [2, 3, 4]:
        print(f'Simulovany {num_games} hry')
    else:
        print(f'Simulovano {num_games} her')

    for i in range(num_games):
        machacek_simulate(num_challenges, enable_output)
        fines = machacek_simulate(num_challenges, enable_output)
        my_list_of_fines[0] += fines[0]
        my_list_of_fines[1] += fines[1]
        my_list_of_fines[2] += fines[2]
    maximum_fines = max(my_list_of_fines)
    most_fined_player = my_list_of_fines.index(maximum_fines) + 1

    print(f' Hrac c.1: {my_list_of_fines[0]} pokut')
    print(f' Hrac c.2: {my_list_of_fines[1]} pokut')
    print(f' Hrac c.3: {my_list_of_fines[2]} pokut')
    print(f'Nejcasteji pokutovanym hracem byl hrac c. {most_fined_player} s {maximum_fines} prohrami')

if __name__ == "__main__":
    machacek_simulate(5, True)
    machacek_stats(5, 5)
