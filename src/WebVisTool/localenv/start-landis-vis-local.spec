# -*- mode: python -*-

block_cipher = None


a = Analysis(['start-landis-vis-local.py'],
             pathex=['C:\\Users\\mshukun\\Documents\\LANDVIZ\\src\\WebVisTool\\localenv'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='start-landis-vis-local',
          debug=False,
          strip=False,
          upx=True,
          console=True )
