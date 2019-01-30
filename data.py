
spotlight_dungeon = 'Thanatos Tower'
spotlight_map = 'pay_fild04'
spotlight_monster_high = 'Eddga'
spotlight_monster_middle = 'Nine Tails'
spotlight_monster_low = 'Poring'

spotlights = f'''The spotlights are:
Dungeon: {spotlight_dungeon}
Map: {spotlight_map}
Monsters: {spotlight_monster_high}, {spotlight_monster_middle}, {spotlight_monster_low}'''

def update_spotlight(payload):
    spotlight_dungeon = payload['spotlight_dungeon']
    spotlight_map = payload['spotlight_map']
    spotlight_monster_high = payload['monster_high']
    spotlight_monster_middle = payload['monster_middle']
    spotlight_monster_low = payload['monster_low']
    return

def post_spotlight_to_discord():
    return spotlights    
