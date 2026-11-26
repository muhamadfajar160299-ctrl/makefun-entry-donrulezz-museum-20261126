import os

# Output dir is taken from MAKEFUN_OUTPUT_DIR (defaults to /output).
LINE = "Parking Meter, c. 2025. Citizens fed it coins to rent the ground their car was already standing on."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
