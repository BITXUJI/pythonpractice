from pathlib import Path

# Path(r"C:\Program Files\Microsoft")
# Path()
path = Path("ecommerce/__init__.py")
# Path()/Path("ecommerce")
# Path()/"ecommerce"/"__init__.py"
# Path.home()
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path1 = path.with_name("file.txt")
print(path1.absolute())
path2 = path.with_suffix(".txt")
print(path2)
