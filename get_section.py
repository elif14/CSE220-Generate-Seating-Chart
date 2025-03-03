import csv 
import sys # for testing purpose to invoke get_section() from command line separately

def get_section (csv_file: str, section: str):
    with open(csv_file, "r") as csv:
        for line in csv:
            print(line)
    section = dict()
    return section

if __name__ == '__main__':
    get_section(sys.argv[1], sys.argv[2])