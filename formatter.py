# formatter.py

from classifier import classify_byte

from classifier import classify_byte

def format_bytes(file_data, remove_non_printable=False):
    formatted_hex = []
    formatted_ascii = []
    lines = []

    for i, byte in enumerate(file_data):
        hex_repr, ascii_repr = classify_byte(byte, remove_non_printable)
        if hex_repr is None:  # Skip non-printable if flag is set
            continue

        formatted_hex.append(hex_repr)
        formatted_ascii.append(ascii_repr)

        if len(formatted_hex) == 16:
            line = f"{i - 15:08X}  {' '.join(formatted_hex)}  |{''.join(formatted_ascii)}|"
            lines.append(line)
            formatted_hex.clear()
            formatted_ascii.clear()

    # Add any remaining bytes (less than 16)
    if formatted_hex:
        line = f"{len(file_data) - len(formatted_hex):08X}  {' '.join(formatted_hex)}  |{''.join(formatted_ascii)}|"
        lines.append(line)

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

