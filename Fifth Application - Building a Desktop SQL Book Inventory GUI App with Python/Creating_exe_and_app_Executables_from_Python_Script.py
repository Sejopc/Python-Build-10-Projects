# This lecture is to learn how to create .exe (Windows) and .app (Mac) files from Python script.

# pip3 install pyinstaller

# pyinstaller --oneline --windowed Connecting_the_frontend_with_backend_part1and2.py

# .exe or .app executuables will be created inside the "dist" folder.

# mv dist/Connecting_the_frontend_with_backend_part1and2.app/ BookStore.app/ -> renames the executable file.


#========== ABOVE WAY OF CREATING THE EXECUTABLE ON MAC, DID NOT WORK FOR ME ==========

# Please follow this one, which worked great:
"""
1) Install py2app
pip install -U py2app

2) Create setup file

py2applet --make-setup myapp.py

3) Open setup.py, change the file's name in the APP variable, put your database's filename in the DATA_FILES variable and save.

APP = ['frontend.py']
DATA_FILES = ['books.db']
4) Build the app

sudo python setup.py py2app

5) Open the app in the folder dist/frontend.app

"""