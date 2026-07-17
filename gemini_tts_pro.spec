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
    a.binaries,
    a.datas,
    [],
    name='GeminiTTSPro',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon='gemini_tts_pro.ico',
)
