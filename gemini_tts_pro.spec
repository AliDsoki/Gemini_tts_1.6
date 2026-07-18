# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['gemini_tts_pro.py'],
    pathex=[],
    binaries=[],
    datas=[('gemini_tts_pro.ico', '.')],
    hiddenimports=['google.genai', 'docx', 'pypdf'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='GeminiTTSPro',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='gemini_tts_pro.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    name='GeminiTTSPro',
)
