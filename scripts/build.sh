#!/bin/bash
set -e

APKTOOL_JAR="apktool.jar"

if [ ! -f "$APKTOOL_JAR" ]; then
    echo "Ошибка: файл $APKTOOL_JAR не найден в текущей папке!"
    exit 1
fi
echo "Используется apktool: $APKTOOL_JAR"

echo "1. Распаковываем оригинальный TikTok..."
java -Xmx8G -jar "$APKTOOL_JAR" d original.apk -o tiktok_workspace -f

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

echo "4.5. Исправляем битые PNG файлы (WebP под видом PNG)..."
python3 patches/fix_png.py

echo "4.6. Исправляем битые XML файлы..."
python3 patches/fix_xml.py

echo "5. Собираем APK обратно (с увеличенным лимитом памяти)..."
java -Xmx8G -jar "$APKTOOL_JAR" b tiktok_workspace -o TikTok_Neo_Unsigned.apk --use-aapt2

echo "6. Выравниваем APK..."
zipalign -v -p 4 TikTok_Neo_Unsigned.apk TikTok_Neo_Aligned.apk

echo "Сборка завершена!"
