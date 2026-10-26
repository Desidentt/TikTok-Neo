#!/bin/bash
set -e

# Указываем, что apktool.jar лежит прямо в корне проекта
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

echo "5. Собираем APK обратно (с увеличенным лимитом памяти)..."
java -Xmx8G -jar "$APKTOOL_JAR" b tiktok_workspace -o TikTok_Neo_Unsigned.apk

echo "6. Выравниваем APK..."
zipalign -v -p 4 TikTok_Neo_Unsigned.apk TikTok_Neo_Aligned.apk

echo "Сборка завершена!"
