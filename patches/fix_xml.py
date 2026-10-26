import os

def fix_xml_files(directory):
    print("Поиск и исправление битых XML файлов...")
    
    # TikTok часто ломает layout-файлы для защиты.
    # d93.xml - известный проблемный файл, вызывающий ошибку aapt2.
    target_file = os.path.join(directory, "layout", "d93.xml")
    
    # Валидный, пустой XML-макет
    valid_xml = """<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">
</LinearLayout>
"""
    
    if os.path.exists(target_file):
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(valid_xml)
        print(f"Исправлен битый XML: {target_file}")
    else:
        print(f"Файл {target_file} не найден, пропускаем.")

if __name__ == "__main__":
    fix_xml_files("tiktok_workspace/res")
