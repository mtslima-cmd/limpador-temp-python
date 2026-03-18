import os

def get_temp_paths():

    # Retorna os caminhos das pastas temporárias do sistema.

    # %temp% -> pasta temporária do usuário
    user_temp = os.environ.get('TEMP')

    # Pasta temp do sistema
    system_temp = r"C:\Windows\Temp"

    return [user_temp, system_temp]