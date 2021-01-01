from pathlib import Path

from zipfile import ZipFile

# zip = ZipFile("files.zip", "w")
# with ZipFile("files.zip", "w") as zip:
#     for path in Path("pythonpractice/ecommerce").rglob("*.*"):
#         zip.write(path)
# zip.close()


with ZipFile("../files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("pythonpractice/ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")
