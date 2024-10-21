from .is_weapon_stat_screen import image_is_weapon_stat_screen
from .find_in_json import find_value_by_id, has_text, get_json

def determine_picture_type(source_text):
    if image_is_weapon_stat_screen(source_text):
        return 'Stats'
    if image_is_weapon_main_screen(source_text=source_text):
        return 'Main'
    if image_is_side_weapon_side_screen(source_text=source_text):
        return 'Side'
    

def image_is_weapon_main_screen(source_text):
    if has_text(source_text=source_text, find_text='ATTACHMENT'):
        return False
    if has_text(source_text=source_text, find_text='WEAPON'):
        return True
        
def image_is_side_weapon_side_screen(source_text):
    if has_text(source_text=source_text, find_text='Floor'):
        return True
