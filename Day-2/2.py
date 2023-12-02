import re

filename = 'input.txt'
input = open(filename, 'r')
orig_data = input.read()
separated_array = orig_data.split('\n')
regex = r"(?<=Game )[0-9]+"
sum_of_games = 0
for x in separated_array:
    id = re.search(regex, x)
    if id:
        game_id = id.group()
        # print(game_id)
    erase_id = re.sub("Game.[0-9]+\:\s", "", x)
    separated_array = erase_id.split('; ')
    for y in separated_array:
        list_of_sets = y.split(', ')
        # print(list_of_sets)
        for z in list_of_sets:
            list_of_picks = z.split(',')
            for k in list_of_picks:
                list_of_balls = k.split(' ')
                # print(list_of_balls)
                amount = int(list_of_balls[0])
                color = list_of_balls[1]
                if ((color == 'green') and (amount <= 13)):
                    addition_ok = True
                    break
                elif ((color == 'blue') and (amount <= 14)):
                    addition_ok = True
                    break
                elif ((color == 'red') and (amount <= 12)):
                    addition_ok = True
                    break
                else:
                    print("ID of error: " + str(game_id) + " Amount: " + str(amount) + " Color: " + str(color))
                    addition_ok = False
                    break
            if addition_ok == False:
                break
        if addition_ok == False:
            break
    if addition_ok:
        sum_of_games += int(game_id)
print(sum_of_games)
