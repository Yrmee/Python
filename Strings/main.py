# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# PART 1: 

# Variables for players
player_one = 'Ruud Gullit'
player_two = 'Marco van Basten'

# Variables for each minute of the match that a goals was scored
goal_0 = 32
goal_1 = 54

# create a string that reports on who scored when
scorers = f'{player_one} {goal_0}, {player_two} {goal_1}'
print(scorers)

# Use f-strings of the + operator to create a single string with information
report = f'{player_one} scored in the {goal_0}nd minute\n' + f'{player_two} scored in the {goal_1}th minute'
print(report)

# PART 2     

# Choose a player and store his name as a string 
player = 'Steven Berghuis'
# Slicing for his first name 
first_name = player[:player.find(" ")]
print(first_name)
# Length Lastname
last_name_len = len(player[player.find(" ") + 1 :])
print(last_name_len)
# isolate and store the players name - exampe: S. Berghuis
name_short = player[0] + '.' + player[player.find(" ") :]
print(name_short)
# chant players name as same as chars.length first name
chant = ((player[:player.find(" ")] + '! ') * len(player[:player.find(" ")]))[:-1]
print(chant)
# 
good_chant = chant[-1] != " "
