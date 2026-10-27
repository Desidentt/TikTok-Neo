import os
import re

def change_package(workspace_dir):
    print("Смена имени пакета...")
    old_pkg = "com.zhiliaoapp.musically"
    new_pkg = "com.tiktokneo.mod"
    
    old_pkg_path = old_pkg.replace(".", "/")
    new_pkg_path = new_pkg.replace(".", "/")

    # 1. Меняем пакет в AndroidManifest.xml
    manifest_path = os.path.join(workspace_dir, "AndroidManifest.xml")
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Заменяем основной пакет
        content = content.replace(f'package="{old_pkg}"', f'package="{new_pkg}"')
        
        # Заменяем пакет во всех authorities (провайдерах), чтобы избежать конфликтов
        content = content.replace(f'{old_pkg}.', f'{new_pkg}.')
        
        with open(manifest_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("AndroidManifest.xml обновлен.")

    # 2. Меняем пути в Smali файлах
    patched_files = 0
    for root, dirs, files in os.walk(workspace_dir):
        for file in files:
            if file.endswith(".smali"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Ищем Lorg/package/path и заменяем на Lnew/package/path
                if old_pkg_path in content:
                    content = content.replace(f'L{old_pkg_path}/', f'L{new_pkg_path}/')
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    patched_files += 1
                        
    print(f"Имя пакета изменено на {new_pkg}. Обновлено файлов Smali: {patched_files}")

if __name__ == "__main__":
    change_package("tiktok_workspace")
