import os

def fix_xml_files(directory):
    print("Поиск и исправление битых XML файлов...")
    target_file = os.path.join(directory, "layout", "d93.xml")
    
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

if __name__ == "__main__":
    fix_xml_files("tiktok_workspace/res")
