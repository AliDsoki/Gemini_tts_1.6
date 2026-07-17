@echo off
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
pip install pyinstaller
pyinstaller gemini_tts_pro.spec --noconfirm
echo.
echo تم البناء. الملف الناتج في مجلد dist\GeminiTTSPro.exe
pause
