python -OO trunk\pyinstaller.py make.spec
python post_build_maker.py
copy dist\make.exe "D:\Multimedia Fusion Developer 2\Data\Runtime\Anaconda\make.exe"
copy dist\extensions.dat "D:\Multimedia Fusion Developer 2\Data\Runtime\Anaconda\extensions.dat"
copy dist\png2ico.exe "D:\Multimedia Fusion Developer 2\Data\Runtime\Anaconda\png2ico.exe"