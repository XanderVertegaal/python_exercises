# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, time_of_day, cows_need_milking, cow_location, season, slurry_tank_is_full, grass_is_long):
    action = ''
    if (cow_location == 'pasture' and time_of_day == 'night') or (cow_location == 'pasture' and weather == 'rainy'):
        action = 'take cows to cowshed'

    elif cows_need_milking == True:
        if cow_location == 'cowshed':
            action = 'milk cows'
        elif cow_location == 'pasture':
            action = 'take cows to cowshed' + '\n' + 'milk cows' + '\n' + 'take cows back to pasture'
    
    elif slurry_tank_is_full == True and (weather not in ['sunny', 'windy']):
        if cow_location == 'cowshed':
            action = 'fertilize pasture'
        elif cow_location == 'pasture':
            action = 'take cows to cowshed' + '\n' + 'fertilize pasture' + '\n' + 'take cows back to pasture'

    elif grass_is_long == True and season == 'spring' and weather == 'sunny':
        if cow_location == 'cowshed':
            action = 'mow grass'
        elif cow_location == 'pasture':
            action = 'take cows to cowshed' + '\n' + 'mow grass' + '\n' + 'take cows back to pasture'

    elif action == '':
        action = 'wait'

    return action


