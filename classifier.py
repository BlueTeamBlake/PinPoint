def classify_byte(byte, remove_non_printable=False):
    # Classify as printable only if the byte is human-readable (for ASCII range)
    if 32 <= byte <= 126:  # Printable ASCII range
        return f"1x{byte:02X}", chr(byte)  # Format in hex and ASCII
    elif byte == 0x00:  # Null byte
        return f"0x{byte:02X}", "."  # Represent null as a dot in ASCII
    else:  # Non-printable
        if remove_non_printable:
            return None, None  # Skip non-printable bytes if flag set to Y
        return f"2x{byte:02X}", "."  # Represent non-printable in hex and dot in ASCII


