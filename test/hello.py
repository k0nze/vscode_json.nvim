import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Hello")
    
    if len(sys.argv) > 1:
        print(f"Hello {' '.join(sys.argv[1:])}")
