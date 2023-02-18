import os

Roaming = os.getenv('APPDATA')

paths = {
    'Discord': Roaming + '\\discord',
    'Discord Canary': Roaming + '\\discordcanary',
    'Discord PTB': Roaming + '\\discordptb',
}

d = 0

for platform, path in paths.items():
    if not os.path.exists(path):
        continue
    if platform == 'Discord':
        for file in os.listdir(path + f"\\Cache\\"):
            try:
                os.remove(f'{path}/Cache/{file}')
                d += 1
                print(f'REMOVED {d}')
            except Exception as error:
                print(str(error))
    else:
        for file in os.listdir(path + f"\\Cache\\Cache_Data"):
            try:
                os.remove(f'{path}/Cache/Cache_Data/{file}')
                d += 1
                print(f'REMOVED {d}')
            except Exception as error:
                print(str(error))