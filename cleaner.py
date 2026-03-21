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

def delete_files(files):
    """
    Tenta apagar os arquivos infromados de forma segura.
    
    Parâmetros:
        files (list): lista com os caminhos dos arquivos
    
    Retorno:
        tuple:
            deleted_count (int): quantidade de arquivos apagados
            failed_count (int): quantidade de arquivos que não puderam ser apagados
            freed_space (int): espaço liberado em bytes
    """

    deleted_count = 0
    failed_count = 0
    freed_space = 0

    for file_path in files:
        try:
            # Pega o tamanho do arquivo antes de apagá-lo
            file_size = os.path.getsize(file_path)

            # Tenta excluir o arquivo
            os.remove(file_path)

            # Se conseguiu apagar, atualiza os contadores
            deleted_count += 1
            freed_space += file_size
        
        except FileNotFoundError:
            # O arquivo pode ter sido removido por outro processo
            failed_count += 1
        
        except PermissionError:
            # Arquivo em uso ou sem permissão para exclusão
            failed_count += 1

        except OSError:
            # Outros erros do sistema operacional
            failed_count += 1
        
        except Exception as e:
            print(f"[ERRO] Falha inesperada ao excluir {file_path}: {e}")
            failed_count += 1
    
    return deleted_count, failed_count, freed_space

def remove_empty_folders(temp_paths):
    """
    Tenta remover subpastas vazias dentro das pastas temporárias.

    Parâmetros:
        temp_paths (list): lista com os caminhos das pastas temporárias

    Retorno:
        int: quantidade de subpastas vazias removidas
    """

    removed_count = 0

    for path in temp_paths:
        # Ignora caminhos vazios ou inexistentes
        if not path or not os.path.exists(path):
            continue

        # Percorre de baixo para cima para tentar remover primeiro as pastas mais internas
        for root, dirs, files in os.walk(path, topdown=False):
            # Não remove a pasta temporária principal
            if root == path:
                continue

            try:
                # Verifica no momento real da tentativa se a pasta está vazia
                if not os.listdir(root):
                    os.rmdir(root)
                    removed_count += 1
                
            except PermissionError:
                # Sem permissão para remover a pasta
                continue

            except OSError:
                # A pasta pode não estar vazia ou estar em uso
                continue

            except Exception:
                # Qualquer outro erro inesperado é ignorado
                continue

    return removed_count

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