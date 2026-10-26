import os
import base64

# 100% валидный 1x1 прозрачный PNG, закодированный в Base64
valid_png_base64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
valid_png_bytes = base64.b64decode(valid_png_base64)

def fix_invalid_pngs(directory):
    print("Поиск и исправление битых PNG файлов...")
    fixed_count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".png"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'rb') as f:
                        header = f.read(8)
                        # Если файл не начинается с сигнатуры PNG
                        if header != b'\x89PNG\r\n\x1a\n':
                            # Перезаписываем его валидным PNG
                            with open(filepath, 'wb') as wf:
                                wf.write(valid_png_bytes)
                            fixed_count += 1
                except Exception as e:
                    print(f"Ошибка при обработке {filepath}: {e}")
    print(f"Всего исправлено: {fixed_count}")

if __name__ == "__main__":
    fix_invalid_pngs("tiktok_workspace/res")
