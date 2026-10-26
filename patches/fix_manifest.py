import re
import os

def fix_manifest(workspace_dir):
    manifest_path = os.path.join(workspace_dir, "AndroidManifest.xml")
    if not os.path.exists(manifest_path):
        return

    print("Удаляем некорректные ссылки на ресурсы в AndroidManifest.xml...")
    with open(manifest_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Полностью удаляем атрибут и его значение (например, android:resource="@123456")
    pattern = r'\s+[\w:]+="@\d+"'
    
    matches = re.findall(pattern, content)
    if matches:
        print(f"Найдено {len(matches)} проблемных атрибутов. Удаляем...")
        content = re.sub(pattern, '', content)
        
        with open(manifest_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Манифест очищен.")
    else:
        print("Проблем не найдено.")

if __name__ == "__main__":
    fix_manifest("tiktok_workspace")
