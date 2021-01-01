from pathlib import Path
path = Path("pythonpractice/ecommerce")
print(path.name)
print(path.absolute())
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")
# for item in path.iterdir():
#     print(item)
# print([path.iterdir()])
paths = [p for p in path.iterdir() if p.is_dir()]
# py_files = [p for p in path.glob("**/*.py")]
py_files = [p for p in path.rglob("*.py")]
print(paths)
print(py_files)
