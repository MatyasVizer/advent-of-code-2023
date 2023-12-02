import re

filename = 'input.txt'
input = open(filename, 'r')
orig_data = input.read()
separated_array = orig_data.split('\n')
regex = r"(?<=Game )[0-9]+"
power_of_games = 0
for x in separated_array:
    id = re.search(regex, x)
    if id:
        game_id = id.group()
        print(game_id + ": ")
    erase_id = re.sub("Game.[0-9]+\:\s", "", x)
    separated_array = erase_id.split('; ')
    green_min = 0
    blue_min = 0
    red_min = 0
    for y in separated_array:
        list_of_sets = y.split(', ')
        # print(list_of_sets)
        for z in list_of_sets:
            list_of_picks = z.split(',')

            for k in list_of_picks:
                list_of_balls = k.split(' ')
                print(list_of_balls)
                amount = int(list_of_balls[0])
                color = list_of_balls[1]
                if (color == 'green'):
                    if green_min < amount:
                        green_min = amount
                        break
                elif (color == 'blue'):
                    if blue_min < amount:
                        blue_min = amount
                        break
                elif (color == 'red'):
                    if red_min < amount:
                        red_min = amount
                        break
    print(green_min)
    print(blue_min)
    print(red_min)
    result = green_min * blue_min * red_min
    print(result)
    power_of_games += result
print(power_of_games)
