import sys
from formatter import format_bytes, save_to_file
from args_parser import parse_arguments

def read_file(file_path: str) -> bytes:
    """
    Reads a binary file and returns its content as bytes.
    """
    try:
        with open(file_path, "rb") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

import sys
from formatter import format_bytes, save_to_file

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
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def main():
    print_banner()  # Display the banner when the program starts
    
    # Prompt for input file
    input_file = input("Enter the path to the input file: ")
    
    # Prompt for output file
    output_file = input("Enter the path to save the formatted output (e.g., 'output.txt'): ")
    
    # Ask whether to remove non-printable bytes
    remove_non_printable_input = input("Remove non-printable bytes? (Y/N): ").strip().lower()
    remove_non_printable = remove_non_printable_input == 'y'

    # Read the file data
    file_data = read_file(input_file)

    # Format the bytes from the file
    formatted_output = format_bytes(file_data, remove_non_printable=remove_non_printable)

    # Save the formatted output to the specified file
    save_to_file(formatted_output, output_file)

if __name__ == "__main__":
    main()
