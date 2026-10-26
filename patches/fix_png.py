import os

def fix_invalid_pngs(directory):
    print("Поиск и УДАЛЕНИЕ битых PNG файлов...")
    removed_count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".png"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'rb') as f:
                        header = f.read(8)
                        if header != b'\x89PNG\r\n\x1a\n':
                            f.close()
                            os.remove(filepath)
                            removed_count += 1
                except Exception as e:
                    pass
    print(f"Всего удалено битых файлов: {removed_count}")

if __name__ == "__main__":
    fix_invalid_pngs("tiktok_workspace/res")
