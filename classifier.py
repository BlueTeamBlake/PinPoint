def classify_byte(byte):
    if byte == 0x00:
        return "0x"  # Null byte
    elif byte in (0x09, 0x0A, 0x0D, 0x20):  # Whitespace: tab, LF, CR, space
        return "0x"
    elif 0x20 <= byte <= 0x7E:  # Printable ASCII
        return "1x"
    elif byte < 0x20 or byte == 0x7F:  # Control characters
        return "0x"
    else:
        return "2x"  # Extended bytes


