# formatter.py

from classifier import classify_byte

from classifier import classify_byte

def format_bytes(data: bytes, remove_non_printable=False) -> str:
    lines = []
    line_size = 16

    for i in range(0, len(data), line_size):
        chunk = data[i:i + line_size]

        hex_chunk = []
        ascii_chunk = []

        for byte in chunk:
            if 32 <= byte <= 126:  # Printable ASCII
                semantic_prefix = "1x"
                char = chr(byte)
                hex_chunk.append(f"{semantic_prefix}{byte:02X}")
                ascii_chunk.append(char)
            else:
                # Non-human-readable
                if remove_non_printable:
                    continue  # Skip it entirely
                semantic_prefix = "0x"
                hex_chunk.append(f"{semantic_prefix}{byte:02X}")
                ascii_chunk.append(' ')  # Space instead of '.' placeholder

        offset = f"{i:08X}"
        hex_str = ' '.join(hex_chunk).ljust(line_size * 5)  # Pad to line width
        ascii_str = ''.join(ascii_chunk)
        lines.append(f"{offset}  {hex_str}  |{ascii_str}|")

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

