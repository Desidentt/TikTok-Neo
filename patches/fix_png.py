import os

valid_png = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82'

def fix_invalid_pngs(directory):
    print("Поиск и исправление битых PNG файлов...")
    fixed_count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".png"):
                filepath = os.path.join(root, file)
                with open(filepath, 'rb') as f:
                    header = f.read(8)
                    if header != b'\x89PNG\r\n\x1a\n':
                        with open(filepath, 'wb') as wf:
                            wf.write(valid_png)
                        fixed_count += 1
    print(f"Всего исправлено: {fixed_count}")

if __name__ == "__main__":
    fix_invalid_pngs("tiktok_workspace/res")
