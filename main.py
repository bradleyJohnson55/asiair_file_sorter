import shutil, os, re
from pathlib import Path

import config

HOME_DIRECTORY = config.HOME_DIRECTORY
SCAN_DIR="raw_dump"

def move_create(f, dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

    shutil.move(f, dir)


def get_filter(f):
    search = re.search("_[A-Z]_", f)
    if search:
        filter = f[search.start()+1]
        return filter
    else:
        print(f"Could not find a filter to assign to file: {f}")


def get_type(f):
    """
    returns the type of file e.g. Light, Flat
    """

    end = f.find('_')
    return f[:end]

def get_date(f):
    """
    parses date from file
    """

    search = re.search("_[0-9]{8}-", f)
    if search:
        date = f[search.start()+1:search.start()+9]
        return date
    else:
        print(f"Could not parse date from file: {f}")
        

def init_project_structure(p):
    """
    initializes the project directory structure
    """

    # make Lights folder
    if not os.path.exists(f"{p}/Lights"):
        os.makedirs(f"{p}/Lights")

    # make Flats folder
    if not os.path.exists(f"{p}/Flats"):
        os.makedirs(f"{p}/Flats")
    
    # make PI folder
    if not os.path.exists(f"{p}/PI"):
        os.makedirs(f"{p}/PI")

    # make bad_subs folder
    if not os.path.exists(f"{p}/bad_subs"):
        os.makedirs(f"{p}/bad_subs")

    # make raw_dump folder
    if not os.path.exists(f"{p}/raw_dump"):
        os.makedirs(f"{p}/raw_dump")

def main():
    project = input('Enter the name of the project directory: ')
    project_base_dir = f"{HOME_DIRECTORY}/{project}"
    init_project_structure(project_base_dir)

    filter = None
    type = None

    for f in os.listdir(f"{project_base_dir}/{SCAN_DIR}"):
        # only want to move FITS files
        if f[-3:] != 'fit':
            continue

        filter = get_filter(f)
        image_type = get_type(f)

        # process Lights
        if get_type(f) == 'Light':
            move_create(f"{project_base_dir}/{SCAN_DIR}/{f}", f"{project_base_dir}/Lights/{filter}")
        # process flats
        elif get_type(f) == 'Flat':
            # parse date from file
            date = get_date(f)
            date = f"{date[:4]}-{date[4:6]}-{date[6:]}"
            move_create(f"{project_base_dir}/{SCAN_DIR}/{f}", f"{project_base_dir}/Flats/{filter}/{date}")
            


main()
