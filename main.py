from cleaner import get_temp_paths

paths = get_temp_paths()

print("Pastas temporárias encontradas:")
for path in paths:
    print(path)