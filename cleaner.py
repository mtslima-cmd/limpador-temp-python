import os

def get_temp_paths():
    """
    Retorna os caminhos das pastas temporárias do sistema
    """

    # %temp% -> pasta temporária do usuário
    user_temp = os.environ.get('TEMP')

    # Pasta temp do sistema
    system_temp = r"C:\Windows\Temp"

    return [user_temp, system_temp]

def get_all_files(temp_paths):
    """
    Percorre as pastas temporárias informadas e retorna uma lista
    com o caminho completo de todos os arquivos encontrados.

    Parâmetros:
        temp_paths (list): lista com os caminhos das pastas temporárias

    Retorno:
        list: lista de arquivos encontrados
    """

    all_files = []

    for path in temp_paths:
        # Ignora caminhos vazios ou inexistentes
        if not path or not os.path.exists(path):
            continue

        try:
            # os.walk percorre a pasta e todas as subpastas
            for root, dirs, files in os.walk(path):
                for file_name in files:
                    full_path = os.path.join(root, file_name)
                    all_files.append(full_path)

        except PermissionError:
            print(f"[AVISO] Sem permissão para acessar: {path}")

        except Exception as e:
            print(f"[ERRO] Problema ao acessar {path}: {e}")

    return all_files

def get_total_size(files):
    """
    Calcula o tamanho total dos arquivos informados.
    
    Parâmetros:
        files (list): lista com os caminhos dos arquivos
    
    Retorno:
        int: tamanho total em bytes
    """

    total_size = 0

    for file_path in files:
        try:
            # Soma o tamanho de cada arquivo
            total_size += os.path.getsize(file_path)
        
        except FileNotFoundError:
            # Arquivo pode ter sido apagado durante execução
            continue

        except PermissionError:
            # Sem permissão para acessar o arquivo
            continue

        except Exception as e:
            print(f"[ERRO] Falha ao obter tamanho de {file_path}: {e}")
    
    return total_size

def format_size(size_bytes):
    """
    Converte um tamanho em bytes para KB, MB ou GB.

    Parâmetros:
        size_bytes (int): tamanho em bytes

    Retorno:
        str: tamanho formatado (ex: 10.5 MB)
    """

    # Lista de unidades
    units = ["B", "KB", "MB", "GB", "TB"]

    size = float(size_bytes) # converte para float (número com casa decimal)
    unit_index = 0

    # Vai dividindo até chegar na unidade ideal
    while size >= 1024 and unit_index  < len(units) - 1:
        size /= 1024
        unit_index += 1

    return f"{size:.2f} {units[unit_index]}"