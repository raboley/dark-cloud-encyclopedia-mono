from FileOs import FileOs
file_path = 'weapons.json'

fileObject = FileOs('/Users/russellboley/Downloads/Git/Dark-Cloud-Website-1/src/api/weapons/')

json = fileObject.read_file('/Users/russellboley/Downloads/Git/Dark-Cloud-Website-1/src/api/weapons/weapons.json')
new_json = fileObject.read_file('/Users/russellboley/Downloads/Git/Dark-Cloud-Website-1/src/api/weapons/weapons.json')

i = 0
for weapon in json:
    new_thumbnail = weapon["weaponThumbnail"].replace(' ', '_')
    new_json[i]["weaponThumbnail"] = new_thumbnail
    i += 1

fileObject.set_json_file(file_path, new_json)

