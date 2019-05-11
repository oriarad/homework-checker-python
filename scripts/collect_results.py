import xml.etree.ElementTree as ET
import os
import sys
import csv

DOT_EXTENSION_LEN = 4
FILENAME_PREFIX_LEN = 13
DEFAULT_PATH = './results'

def parse_results_file(filepath):
    """
    Parse a single results file
    
    :param filepath: The full path of the file to parse
    :returns: A tuple of (student, tests) where student is a dictionary that
        represents a single student's results, and the tests is a list of all
        executed tests for that student.
    """
    root = ET.parse(filepath).getroot()
    tests = []
    failed = int(root.attrib['errors']) + \
             int(root.attrib['failures']) + \
             int(root.attrib['skip'])
    student = {'failed':failed}
    for child in root:
        student[child.attrib['name']] = False if len(child) > 0 else True
        tests.append(child.attrib['name'])
    return student, tests


def parse_all_files(path):
    """
    Iterates over all tests result files, and parse the info from them
    
    :param path: A path to the directory where all results files located.
    :returns: A tuple of (students, tests) where students is a list of the
        student's results, and the tests is a list of all executed tests.
    """
    students = []
    tests_names = set()
    for dirpath, dnames, fnames in os.walk(path):
        for file in fnames:
            if file.endswith(".xml"):
                filepath = os.path.join(dirpath, file)
                student, tests = parse_results_file(filepath)
                tests_names.update(tests)
                student['name'] = file[FILENAME_PREFIX_LEN:-DOT_EXTENSION_LEN]
                students.append(student)
    return students, sorted(list(tests_names))

def create_summary(students, tests_names, filename = 'results.csv'):
    """
    Creates a CSV file that summerize all the testing results
    
    :param students: All students results
    :param tests_names: All executed tests
    :param filename: Output filename
    """    
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['name', 'failed'] + tests_names
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for student in students:
            writer.writerow(student)

def main():
    path = DEFAULT_PATH
    if len(sys.argv) > 1: path = sys.argv[1]
    students, tests_names = parse_all_files(path)
    create_summary(students, tests_names)

if __name__ == '__main__':
    main()
