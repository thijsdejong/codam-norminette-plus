""" Function to check for updates """
import urllib
from const import VERSION, VERSIONFILE, UPDATECOMMAND

UPDATE_FAIL = "\n" + "\033[31m" + "Update:" + "\033[0m "
UPDATE_WARN = "\n" + "\033[33m" + "Update:" + "\033[0m "

def update():
    """ Functions compares local version to latest version """
    try:
        raw_version = urllib.urlopen(VERSIONFILE)
    except IOError as e:
        print UPDATE_FAIL + "can't fetch version file: " + str(e)
    else:
        if raw_version.getcode() == 200:
            local_version = raw_version.read().rstrip()
            if local_version != VERSION:
                print(UPDATE_WARN + "version " + local_version + " is available, you have version "
                      + VERSION + "\n\t" + "to update run: " + UPDATECOMMAND)
        else:
            print UPDATE_FAIL + "can't fetch version file"
