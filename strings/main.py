# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line


# Part 1
player_0 = 'Ruud Gullit'
player_1 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = player_0 + " " +  str(goal_0) + ", "  + player_1 + " " + str(goal_1)


report = f"{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute"

# Part 2
player = 'Gerald Vanenburg'

first_name = player[player.find('Gerald'): 6]
print(first_name)

# alternative:
#first_name = player.split()[0] 


last_name_len  = len(player[player.find('Vanenburg'):])

# alternative (hardcoded)
#last_name_len = len(player[7:])


name_short = f"{player[0]}. {player[7:]}"

chant = f"{player[0:6]}! {player[0:6]}! {player[0:6]}! {player[0:6]}! {player[0:6]}! {player[0:6]}!"

good_chant = player[-1] != ''








