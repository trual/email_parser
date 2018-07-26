#!/usr/bin/python
from parser import Parser
import argparse

DEFAULT_ARCHIVE = "sampleEmails4.tar"
DEFAULT_OUTPUT = "archive_metadata.txt"

def main():
    ### take in args for out/inputarchive
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-i", "--input_file",
                    help="tar file to read")
    arg_parser.add_argument("-o", "--output_file",
                    help="output file to write")
    args = arg_parser.parse_args()
    if args.input_file:
        input_file = args.input_file
    else:
        input_file = DEFAULT_ARCHIVE
    if args.output_file:
        output_file = args.output_file
    else:
        output_file = DEFAULT_OUTPUT

    p = Parser()
    p.parse_archive(input_file, output_file)


if __name__ == '__main__':
    main()
