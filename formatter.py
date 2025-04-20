# formatter.py

from classifier import classify_byte

from classifier import classify_byte

def format_bytes(byte_data, bytes_per_line=16, remove_non_printable=False):
    lines = []

    for i in range(0, len(byte_data), bytes_per_line):
        chunk = byte_data[i:i + bytes_per_line]
        hex_bytes = []
        ascii_chars = []

        for byte in chunk:
            # Hex view: Always include every byte
            hex_bytes.append(f"{byte:02x}")

            # ASCII view
            if 0x20 <= byte <= 0x7E:  # Printable ASCII
                ascii_chars.append(chr(byte))
            else:
                if remove_non_printable:
                    ascii_chars.append(' ')  # Replace with space
                else:
                    ascii_chars.append('.')  # Keep dot for visibility

        hex_part = ' '.join(hex_bytes).ljust(bytes_per_line * 3)
        ascii_part = ''.join(ascii_chars)
        lines.append(f"{hex_part} | {ascii_part}")

    return '\n'.join(lines)

def save_to_file(formatted_data: str, output_file: str):
    """
    Saves the formatted byte data to a text file.
    """
    try:
        with open(output_file, 'w') as file:
            file.write(formatted_data)
        print(f"Formatted data saved to {output_file}")
    except Exception as e:
        print(f"Error saving to file: {e}")

