from classifier import classify_byte

def format_bytes(byte_data, bytes_per_line=16):
    lines = []
    for i in range(0, len(byte_data), bytes_per_line):
        chunk = byte_data[i:i+bytes_per_line]
        hex_chunk = []
        ascii_chunk = []

        for b in chunk:
            prefix = classify_byte(b)
            hex_chunk.append(f"{prefix}{b:02X}")
            if 32 <= b <= 126:
                ascii_chunk.append(chr(b))
            else:
                ascii_chunk.append(".")

        hex_str = ' '.join(hex_chunk)
        ascii_str = ''.join(ascii_chunk)
        
        # Calculate spacing so the | aligns consistently
        padding = (bytes_per_line - len(chunk)) * 5  # "1xFF " = 5 characters per byte
        hex_str_padded = hex_str + ' ' * padding
        line = f"{i:08X}  {hex_str_padded} |{ascii_str}|"
        lines.append(line)

    return '\n'.join(lines)

