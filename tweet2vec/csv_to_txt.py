import csv
import argparse
import os
from pathlib import Path

def get_args_from_command_line():
    """Parse the command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_csv_path", type=str)
    parser.add_argument("--text_column_order", type=int)
    args = parser.parse_args()
    return args

args = get_args_from_command_line()

output_path = os.path.dirname(args.input_csv_path)
txt_file_name = Path(args.input_csv_path).stem + '.txt'

output = open(os.path.join(output_path,txt_file_name), 'w')

with open(args.input_csv_path) as f:
    readCsv = csv.reader(f)
    for row in readCsv:
        output.write("%s\n" % row[args.text_column_order].lower())

output.close()