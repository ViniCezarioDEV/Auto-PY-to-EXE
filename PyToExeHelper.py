import os
import PyInstaller.__main__
import time
ScriptSelected = None
DistPath = os.getcwd()
Mode = None
Icon = None
def logo():
    print(
        '''
█████▄░██░░██░░░████████░▄█████▄░░░▄█████░██░░██░▄█████
██░░██░██░░██░░░░░░██░░░░██░░░██░░░██░░░░░██░░██░██░░░░
█████▀░▀████▀░░░░░░██░░░░██░░░██░░░█████░░░████░░█████░
██░░░░░░░██░░░░░░░░██░░░░██░░░██░░░██░░░░░██░░██░██░░░░
██░░░░░░░██░░░░░░░░██░░░░▀█████▀░░░▀█████░██░░██░▀█████
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░''')

def info():
    global ScriptSelected, DistPath, Mode, Icon
    print(f'''
    Script Selected: {ScriptSelected}
    DistPath: {DistPath}
    Mode: {Mode}
    Icon: {Icon}
''')

def listScripts():
    global ScriptSelected
    list = os.listdir()
    scriptList = []
    for i in list:
        if '.py' in i:
            scriptList.append(i)
    if scriptList:
        for i, j in enumerate(scriptList):
            print(f'[{i + 1}] {j}')
        choice = int(input('Choose the Script >>> ')) - 1
        ScriptSelected = scriptList[choice]
        os.system('cls')
        logo()
        info()
    else:
        print('.py Files not exists')
        input('Enter to Close')
        exit()

def changeDistPath():
    global DistPath
    i = input('New DistPath (Enter to keep current DistPath) >>> ')
    if i == '':
        pass
    else:
        DistPath = i
    os.system('cls')
    logo()
    info()

def mode():
    global Mode
    i = input('Select Mode (console) (windowed) >>> ').lower()
    if i == 'console':
        Mode = i
    elif i == 'windowed':
        Mode = i
    else:
        mode()
    os.system('cls')
    logo()
    info()

def listIcons():
    global Icon
    list = os.listdir()
    iconList = []
    for i in list:
        if '.ico' in i:
            iconList.append(i)
    if iconList:
        for i, j in enumerate(iconList):
            print(f'[{i + 1}] {j}')
        choice = input('Choose the Icon (Enter to keep without Icon) >>> ')
        if choice == '':
            withoutIcon() #convert without icon
        else:
            Icon = iconList[int(choice)-1]
            withIcon() #convert with icon
    else:
        print('.ico Files not exists')
        for i in range(3):
            time.sleep(1)
            print(f'Continuing without Icon')
        withoutIcon()

def withIcon():
    print('WORKING WITH ICON')
    global ScriptSelected, Mode, DistPath, Icon
    PyInstaller.__main__.run([
        f'{ScriptSelected}',
        '--onefile',
        f'--{Mode}',
        '--distpath', fr'{DistPath}',
        '--icon', fr'{Icon}'
    ])

def withoutIcon():
    print('WORKING WITHOUT ICON')
    global ScriptSelected, Mode, DistPath
    PyInstaller.__main__.run([
        f'{ScriptSelected}',
        '--onefile',
        f'--{Mode}',
        '--distpath', fr'{DistPath}'
    ])

logo()
info()
listScripts()
changeDistPath()
mode()
listIcons()
remove = []
removeList = []
removeList = os.listdir()
for i in removeList:
    if '.spec' in i:
            remove.append(i)
os.system('rmdir /s build')
os.remove(remove[0])
input('Enter to Close')