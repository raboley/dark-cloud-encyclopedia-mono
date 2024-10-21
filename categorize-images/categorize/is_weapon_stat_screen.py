import json
import difflib
from .find_in_json import find_value_by_id, has_text, get_json


def image_is_weapon_stat_screen(source_text):
    if has_text(source_text=source_text, find_text='ATTACHMENT'):
        return True
    else:
        return False
        
def get_weapon_name(source_text, id=4, weapon_list='', source_name=''):
    ids_to_check = [4,3,5,2,6,1,7]
    no_valid_weapon_name_error = 'Couldnt find a valid weapon name in: "'+ source_name + '" from any of these: '
    for id in ids_to_check:
        raw_weapon_name = find_value_by_id(source_text=source_text, id=id)
        final_weapon_name = raw_weapon_name.split('+')[0]
        if weapon_list:
            closest_weapon = difflib.get_close_matches(final_weapon_name, weapon_list, 1)
            if closest_weapon:
                final_weapon_name = closest_weapon[0]
                return final_weapon_name
            else:
                no_valid_weapon_name_error += final_weapon_name + ';'
    raise ValueError(no_valid_weapon_name_error)

def get_weapon_list(weapon_list_json):
    weapons = []
    for weapon in weapon_list_json:
        weapons.append(weapon["Weapon Name"])
    return weapons

def determine_character(weapon_name, weapon_map_json):
    character_name = next((item for item in weapon_map_json if item["Weapon Name"] == weapon_name), 'unknown')
    return character_name["Character Name"]

def write_weapon_map_to_file(parent_folder, weapon_name, pair):
    pair.set_pair(parent_folder, weapon_name)
    
def get_final_file_name():
    pass
        #image_type = 'weapon_stat_screen'
        #character_name = 'toan'