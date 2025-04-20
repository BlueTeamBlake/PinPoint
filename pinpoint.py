import sys
from formatter import format_bytes

def print_banner():
    print(r"""
    ╔════════════════════════════════════════════╗
    ║                Pinpoint v1.0               ║
    ║     Human-Readable Hex + ASCII Analyzer    ║
    ║       Classifies & Filters Byte Types      ║
    ╚════════════════════════════════════════════╝
    """)

def read_file(file_path: str) -> bytes:
    """
    Reads a binary file and returns its content as bytes.
    """
    try:
        with open(file_path, "rb") as f:
            return f.read()
    except FileNotFoundError:
        print(f"[!] Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Error reading file: {e}")
        sys.exit(1)

def main():
    print_banner()

    input_path = input("[?] Enter the path to the input file: ").strip()
    output_path = input("[?] Enter the path to save the output file (default: output.txt): ").strip()
    if not output_path:
        output_path = "output.txt"

    byte_data = read_file(input_path)
    formatted_output = format_bytes(byte_data)

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(formatted_output)
        print(f"[+] Hex view saved to: {output_path}")
    except Exception as e:
        print(f"[!] Error writing to file: {e}")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
