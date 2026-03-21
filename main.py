from cleaner import get_temp_paths, get_all_files, get_total_size, format_size

def main():
    temp_paths = get_temp_paths()

    print("Pastas temporárias encontradas:")
    for path in temp_paths:
        print(f"- `{path}")
    
    all_files = get_all_files(temp_paths)

    print ("\nArquivos temporários encontrados:")
    print (f"Total de arquivos: {len(all_files)}")

    # Calcular o tamanho total
    total_size = get_total_size(all_files)
    formatted_size = format_size(total_size)

    print(f"Tamanho total: {formatted_size}") 

    # Mostra apenas os 10 primeiros para não poluir o terminal
    print("\nExemplos de arquivos encontrados:")
    for file_path in all_files[:10]:
        print(f"- {file_path}")

if __name__ == "__main__":
    main()