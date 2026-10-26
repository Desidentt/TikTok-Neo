import os
import re

def patch_smali_files(directory):
    print("Поиск и замена рекламных вызовов в Smali...")
    
    # ЗАГЛУШКА: Позже мы заменим это на реальные классы TikTok
    search_pattern = r"invoke-virtual \{.*\}, L.*->showAd\(\)V"
    replace_pattern = r"# Реклама отключена модом TikTok Neo"
    
    patched_count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".smali"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if re.search(search_pattern, content):
                    new_content = re.sub(search_pattern, replace_pattern, content)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Запатчен файл: {filepath}")
                    patched_count += 1
                    
    print(f"Всего запатчено файлов: {patched_count}")

if __name__ == "__main__":
    patch_smali_files("tiktok_workspace")
