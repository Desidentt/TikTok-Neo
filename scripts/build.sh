#!/bin/bash
set -e

APKTOOL_JAR="apktool.jar"

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

echo "4. Применяем патчи Smali (реклама)..."
python3 patches/remove_ads.py

echo "4.5. ИСПРАВЛЯЕМ битые PNG файлы..."
python3 patches/fix_png.py

echo "4.6. ИСПРАВЛЯЕМ битые XML файлы..."
python3 patches/fix_xml.py

echo "4.7. ОЧИЩАЕМ AndroidManifest.xml..."
python3 patches/fix_manifest.py

echo "4.8. МЕНЯЕМ ИМЯ ПАКЕТА (через apktool.yml)..."
# Вместо прямого редактирования, используем правильный метод apktool
sed -i 's/^renameManifestPackage:.*/renameManifestPackage: com.tiktokneo.mod/' tiktok_workspace/apktool.yml || echo "renameManifestPackage: com.tiktokneo.mod" >> tiktok_workspace/apktool.yml

echo "5. Собираем APK обратно..."
java -Xmx8G -jar "$APKTOOL_JAR" b tiktok_workspace -o TikTok_Neo_Unsigned.apk --use-aapt2

echo "Сборка завершена!"
