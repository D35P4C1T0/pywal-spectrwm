import os
import pprint
import json
from shutil import copyfile

def hexColors(color):
    return (color[:3] + '/' + color[3:5] + '/' + color[5:]).translate({ord('#'): 'rgb:'})
    # '#123456' to 'rgb:12/34/56'

pywal = {'background':'','text':''}
with open(os.environ["HOME"] + "/.cache/wal/colors.json", "r") as jsonColors:
    data = json.load(jsonColors)['colors']
    pywal['background'] = hexColors(data['color0'])
    pywal['text'] = hexColors(data['color7'])

newPath = os.environ["HOME"] + "/.config/spectrwm/spectrwm.conf"
oldPath = os.environ["HOME"] + "/.config/spectrwm/spectrwm.conf.backup"

copyfile(newPath, oldPath) 
with open(oldPath) as old:
    with open(newPath, "w") as new:
        for line in old:
            if('bar_color[1]' in line):
                if(line[0] != '#'):
                    moddedBg = 'bar_color[1] = ' + pywal['background'] + '\n'
                    print('found background')
                    new.write(moddedBg)
            elif('bar_font_color[1]' in line):
                if(line[0] != '#'):
                    moddedFontColor = 'bar_font_color[1] = ' + pywal['text'] + '\n'
                    print('found text color')
                    new.write(moddedFontColor)
            else: new.write(line)
print('Done')
