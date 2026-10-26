#!/bin/bash
set -e

echo "1. Распаковываем оригинальный TikTok..."
apktool d original.apk -o tiktok_workspace -f

echo "2. Меняем название на TikTok Neo..."
sed -i 's/<string name="app_name">.*<\/string>/<string name="app_name">TikTok Neo<\/string>/g' tiktok_workspace/res/values/strings.xml || true

echo "3. Заменяем иконку приложения..."
for dir in tiktok_workspace/res/mipmap-*; do
    if [ -d "$dir" ]; then
        cp assets/logo.png "$dir/ic_launcher.png" || true
    fi
done

echo "4. Применяем патчи Smali..."
python3 patches/remove_ads.py

echo "5. Собираем APK обратно..."
apktool b tiktok_workspace -o TikTok_Neo_Unsigned.apk

echo "6. Выравниваем APK..."
zipalign -v -p 4 TikTok_Neo_Unsigned.apk TikTok_Neo_Aligned.apk

echo "Сборка завершена!"
