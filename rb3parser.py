import time
from pathlib import Path

if __name__ == "__main__":
    before = time.perf_counter()
    input = Path("rb3dlc.txt").read_text()
    
    lines = input.splitlines()
    num = 1
    for line in lines:
        if "Maroon 5" in line:
            print(num, line)
        num += 1