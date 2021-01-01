from pathlib import Path
from time import ctime
import shutil
path = Path("pythonpractice/ecommerce/__init__.py")
path1 = path/"__init__.py"
shutil.copy(path, path1)
# copy execution
# path.exists()
# path.rename("init.txt")
# path.unlink()
print(ctime(path.stat().st_ctime))
with open("pythonpractice/ecommerce/__init__.py", "r") as file:
    pass

print(path.read_text())
path.write_text("print(\"ok\")")
# path.write_bytes()
print(path.read_text())
