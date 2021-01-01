import subprocess
result = subprocess.run(["python", "other.py"],
                        capture_output=True,
                        text=True)

# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen()
print(type(result))
print("args", result.args)
print("returncode", result.returncode)
print("stderr", result.stderr)
print("stdout", result.stdout)
if result.returncode != 0:
    print(result.stderr)
