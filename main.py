from cleaner import (
    get_temp_paths,
    get_all_files,
    get_total_size,
    format_size,
    delete_files,
    remove_empty_folders
)

def main():
    # Busca os caminhos das pastas temporárias
    temp_paths = get_temp_paths()

    # Busca todos os arquivos dentro das pastas temporárias
    all_files = get_all_files(temp_paths)

    # Quantidade total de arquivos encontrados
    total_files = len(all_files)

    # Tamanho total ocupado pelos arquivos encontrados
    total_size = get_total_size(all_files)

    # Tenta apagar os arquivos e recebe o resultado da limpeza
    deleted_count, failed_count, freed_space = delete_files(all_files)

    # Remove subpastas vazias que sobraram após a exclusão dos arquivos
    remove_empty_folders(temp_paths)

    # Exibe o relatório final
    print("\n===== RELATÓRIO DA LIMPEZA =====")
    print(f"Quantos arquivos encontrou: {total_files}")
    print(f"Quanto espaço eles ocupam: {format_size(total_size)}")
    print(f"Quantos arquivos apagou: {deleted_count}")
    print(f"Quantos não conseguiu apagar: {failed_count}")
    print(f"Quanto espaço foi liberado: {format_size(freed_space)}")

if __name__ == "__main__":
    main()