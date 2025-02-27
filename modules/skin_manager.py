import os
import getpass
# import subprocess

username = getpass.getuser()

# Проверяем скин из конфиг файла
def check_skin(config_data):
    

def find_osu_exe_directory(start_directory):
    for root, dirs, files in os.walk(start_directory):
        if 'osu!.exe' in files:
            return root  # Возвращаем путь к директории, где находится файл
    return None

# Проверяем конкретный путь для osu-wine
osu_wine_path = os.path.expanduser("~/.local/share/osu-wine/osu!/osu!.exe")

if os.path.isfile(osu_wine_path):
    print(f"Ты используешь osu-wine: /home/{username}/.local/share/osu-wine/osu!")
    check_skin(osu_wine_path)
else:
    # Если osu-wine не найден, ищем через функцию
    start_directory = os.path.expanduser('~')
    osu_directory = find_osu_exe_directory(start_directory)

    if osu_directory:
        check_skin(osu_directory)
    else:
        print("sosal?")

