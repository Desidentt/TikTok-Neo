import re
import os

def fix_manifest(workspace_dir):
    manifest_path = os.path.join(workspace_dir, "AndroidManifest.xml")
    if not os.path.exists(manifest_path):
        print("AndroidManifest.xml не найден, пропускаем.")
        return

    print(f"Исправляем некорректные ссылки на ресурсы в {manifest_path}...")
    with open(manifest_path, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'(=")@\d+(")'
    matches = re.findall(pattern, content)
    if matches:
        print(f"Найдено {len(matches)} проблемных атрибутов. Заменяем на @null...")
        content = re.sub(pattern, r'\1@null\2', content)
        
        with open(manifest_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Манифест успешно очищен.")
    else:
        print("Проблемных атрибутов не найдено.")

if __name__ == "__main__":
    fix_manifest("tiktok_workspace")
