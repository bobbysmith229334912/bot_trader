import os

print("Checking Python version...")
python_version = os.popen('python --version').read()
print(python_version)

if "Python 3" not in python_version:
    print("Python 3 is not installed. Please install Python 3 from the 'install first' folder and try again.")
    exit()

libraries = ['ccxt', 'pandas', 'matplotlib', 'tkinter']
for library in libraries:
    print(f"Installing {library}...")
    os.system(f'pip install {library}')

print("All necessary libraries have been installed. You can now run trading_bot.py.")
