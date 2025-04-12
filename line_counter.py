# line_counter.py
def count_lines(filepath):
    with open(filepath, "r") as f:
        return sum(1 for _ in f)


if __name__ == "__main__":
    filename = "example.txt"  # Replace with your file name
    print(f"Total lines in {filename}: {count_lines(filename)}")
