#!/bin/bash
set -e

APKTOOL_JAR="apktool.jar"

echo "1. Распаковываем оригинальный TikTok (БЕЗ ТРОГАНИЯ РЕСУРСОВ)..."
java -Xmx8G -jar "$APKTOOL_JAR" d original.apk -o tiktok_workspace -f -r

echo "2. Применяем патчи Smali..."
python3 patches/remove_ads.py

echo "3. ВНЕДРЯЕМ ОБХОД ПРОВЕРКИ ПОДПИСИ (Signature Killer)..."
python3 patches/signature_killer.py

echo "4. Собираем APK обратно (БЕЗ КОМПИЛЯЦИИ РЕСУРСОВ)..."
java -Xmx8G -jar "$APKTOOL_JAR" b tiktok_workspace -o TikTok_Neo_Unsigned.apk

echo "Сборка завершена!"
