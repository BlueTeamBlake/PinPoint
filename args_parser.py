import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Hex Viewer")
    parser.add_argument('input_file', help="Input file to process")
    parser.add_argument('output_file', help="Output file to save results")  
    parser.add_argument('--remove_non_printable', action='store_true', help="Remove non-printable bytes from output")
    return parser.parse_args()

