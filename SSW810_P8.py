# SSW810 HomeWork Week 8
# Xiangyu Wang

from datetime import datetime, timedelta
import os
from collections import defaultdict
from prettytable import PrettyTable


# Part_1
def date_arithmetic():
    # The date three days after Feb 27, 2000
    three_days_after_02272000 = datetime.strptime('02 27 2000', '%m %d %Y') + timedelta(days=3)
    # The date three days after Feb 27, 2017
    three_days_after_02272017 = datetime.strptime('02 27 2017', '%m %d %Y') + timedelta(days=3)
    # Days passed between Jan 1, 2017 and Oct 31, 2017
    days_passed_01012017_10312017 = datetime.strptime('10 31 2017', '%m %d %Y') - \
                                    datetime.strptime('01 01 2017', '%m %d %Y')
    return three_days_after_02272000, three_days_after_02272017, days_passed_01012017_10312017


def file_reading_gen(path, fields, sep=',', header=False):
    try:
        fp = open(path, 'r')  # Open file

    except FileNotFoundError:
        print("Can't open", path)  # Raise exception if the specified file can’t be opened for reading

    else:
        line_number = 0
        if header:
            next(fp)
            line_number += 1

        for line in fp:

            line = line.strip()  # Strip white spaces
            values = line.split(sep)  # Split up lines(cwid, name, major)
            line_number += 1
            if len(values) != fields:

                raise ValueError(
                    # The exception message should include the line number in the file where the problem occurred
                    f' ValueError: {path} has {len(values)} fields on line {line_number} but expected {len(values)}')
            else:

                yield values


class FileAnalyzer:
    """ Searching the directory for Python files """

    def __init__(self, directory):
        """ Get the directory and save file names in it as a dictionary."""
        self.directory = directory  # NOT mandatory!
        self.files_summary = dict()
        for files in os.listdir(directory):
            path = os.path.join(directory, files)
            self.files_summary[path] = dict()
        self.analyze_files()  # summerize the python files data

    def analyze_files(self):
        """ Analyze files and save the number of line,chart,function,class to the subdictionary."""
        for path in self.files_summary:
            try:
                fp = open(path, 'r')
            except FileNotFoundError:
                print("Can't open", path)
            else:

                line_num = 0
                char_num = 0
                func_num = 0
                class_num = 0
                for line in fp:

                    line_without_white = line.strip()
                    line_num += 1
                    char_num += len(line)
                    if line_without_white.startswith('def '): # the number of Python functions
                        func_num += 1

                    if line_without_white.startswith('class '): # the number of Python classes
                        class_num += 1

                self.files_summary[path]['class'] = class_num
                self.files_summary[path]['function'] = func_num
                self.files_summary[path]['line'] = line_num
                self.files_summary[path]['char'] = char_num

    def pretty_print(self):
        """ Using PrettyTable package."""
        prettytable = PrettyTable(field_names=['File Name', 'Classes', 'Functions', 'Lines', 'Characters'])
        for f in self.files_summary:
            prettytable.add_row(
                [f, self.files_summary[f]['class'], self.files_summary[f]['function'], self.files_summary[f]['line'],
                 self.files_summary[f]['char']])

        print(prettytable)