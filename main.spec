# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    hookspath=['.'],
    pathex=['.'],  # Ruta raíz donde está tu proyecto
    binaries=[],
    datas=[
        ('data', 'data'),
        ('utils', 'utils'),
        ('notebooks', 'notebooks')
    ],
    hiddenimports=['unidecode'],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='TECNORED - Punto de Venta',  # Nombre del ejecutable
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Cambiar a True si necesitas consola para depuración
    icon='./data/logo.ico', 
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,  # Corregido
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,  # Incluye los datos
    strip=False,
    upx=True,
    name='punto'  # Nombre de la carpeta de la aplicación
)
