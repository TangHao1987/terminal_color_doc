import csv
import os

__location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():

    color_dict = {}
    with open(os.path.join(__location__, 'color_define.csv'), 'rt') as color_define:
        reader = csv.reader(color_define)
        for row in reader:
            color_dict[row[0]] = row[1]

    config = {}
    with open(os.path.join(__location__, 'terminal_config.csv'), 'rt') as config_define:
        reader = csv.reader(config_define)
        for row in reader:
            config[row[0]] = color_dict.get(row[1])
    with open(os.path.join(__location__, 'doc'), 'rt') as input:
        lines = input.readlines()
        for line in lines:
            split_index = line.find(" ")
            command = line[:split_index]
            if command in config:
                text = line[split_index:].strip()
                print_line(text, config.get(command))
            else:
                print_line(line.strip(), None)
    input.close()
    # read document and print on terminal


def print_line(text, config_obj):

    if config_obj is None:
        print(text)
    else:
        print('\x1b[{0}m{1}\x1b[0m'.format(config_obj, text))


if __name__ == "__main__":
    main()
