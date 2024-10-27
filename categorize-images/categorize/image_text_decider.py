def determine_picture_type(source_text):
    if image_is_weapon_stat_screen(source_text):
        return 'Stats'
    if image_is_weapon_main_screen(source_text=source_text):
        return 'Main'
    if image_is_side_weapon_side_screen(source_text=source_text):
        return 'Side'

def image_is_weapon_stat_screen(source_text):
    if has_text(source_text=source_text, find_text='ATTACH'):
        return True

def image_is_weapon_main_screen(source_text):
    if has_text(source_text=source_text, find_text='ATTACH'):
        return False
    if has_text(source_text=source_text, find_text='WEAPON'):
        return True

    return False

def image_is_side_weapon_side_screen(source_text):
    if has_text(source_text=source_text, find_text='Floor'):
        return True
    if has_text(source_text=source_text, find_text='Floid'):
        return True
    if has_text(source_text=source_text, find_text='speed'):
        return True

    return False

def has_text(source_text, find_text):
    """
    Checks if the substring exists within the text, case insensitive.

    :param source_text: The main text to search within.
    :param find_text: The substring to search for.
    :return: True if the substring exists within the text, False otherwise.
    """
    return find_text.lower() in source_text.lower()
