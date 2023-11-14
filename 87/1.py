# Shutil Module

import shutil

# copy file
shutil.copy("main.py", "main2.py")

# #copy folder
shutil.copytree("1", "mytutorial")

# move file
shutil.move("1", "Shutil.py")

# delete file/folder
shutil.rmtree("mytutorial")
