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

    # Регулярное выражение для поиска атрибутов со значением вида "@123456789"
    # и их удаления (замены на пустую строку).
    # Пример: android:resource="@1292435456" -> ""
    pattern = r'\s+[\w:]+="@\d+"'
    
    # Считаем количество совпадений для отчёта
    matches = re.findall(pattern, content)
    if matches:
        print(f"Найдено {len(matches)} проблемных атрибутов. Удаляем...")
        # Удаляем все совпадения
        content = re.sub(pattern, '', content)
        
        with open(manifest_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Манифест успешно очищен.")
    else:
        print("Проблемных атрибутов не найдено.")

if __name__ == "__main__":
    fix_manifest("tiktok_workspace")
