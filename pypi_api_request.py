# Challenge: Create a bash or Python script that prints out the version of a passed (argument to the script) Python package using https://pypi.org/pypi/
# All code: John Bailey

# steps:
# take input from stdin
#     optparse is deprecated; use argparse
# validate input
# format requests
# send to pypi
#     assumes requests in installed from pypi
#     - pip install requests
# parse json return for latest version
# return version to stdout

import re
import requests
import argparse

# query pypi API to return the latest version of a package
# input lowercase alpha package name
# 
def get_version(package: str) -> str:
    # sanitize package with re
    # PEP 8 guidelines are all lowercase with underscores, but
    # I noticed that there are quite a few packages on pypi that
    # don't follow this convention
    if not re.match('^[A-Za-z]+[A-Za-z_-]+$', package):
        return 'ERROR: Invalid package name'

    # send GET request to pypi
    output = requests.get(f'https://pypi.org/pypi/{package}/json')

    # parse JSON output and return
    if output.status_code == 200:
        data = output.json()
    else:
        return f'ERROR: {str(output.status_code)}'
    return data['info']['version']

# set up some asserts to test get_version() quickly
def test_get():
    try:
        assert get_version('pip') == '21.0.1', 'return valid version'
        assert get_version('asdfadse') == 'ERROR: 404', 'unknown package'
        assert get_version('Package.name') == 'ERROR: Invalid package name'
        return 'test success'
    except AssertionError:
        return 'test fail'

# get args from the command line
# run test_get() if TEST is given
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('package', help='A valid pypi package name')
    args = parser.parse_args()

    if args.package == 'TEST':
        print(test_get())
    else:
        print(get_version(args.package))