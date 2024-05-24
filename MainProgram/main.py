from MultiOrgs.ListChildOrgs import returnChildOrgs
from Users.ListUsers import returnUsers
from Tools.FileWriter import writeToFile
from Tools.FileCleaner import cleanFile
import logging
import json
from datetime import time
import time

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


def main(API_KEY_ID, API_KEY):
    """
    Runs the main program.
    :return:
    """
    logger = logging.getLogger('Running main program')
    logger.info("fetching child_orgs")
    file_path = 'Files/results.json'
    # file_name = file_path.split('/')[1]
    child_org_list = returnChildOrgs(API_KEY_ID, API_KEY)
    if child_org_list:
        # Cleans the file before start writing to it.
        cleanFile(file_path)
    for org in child_org_list:
        data = returnUsers(API_KEY_ID, API_KEY, org)
        writeToFile(file_path, data)
        # Pauses the "returnUsers()" module for 5 seconds to not hit rate limiting.
        time.sleep(5)


if __name__ == '__main__':
    API_KEY_ID = "2893a77986cc4340a78733f077db2448"
    API_KEY = "ed0ee232eae448ef9d610dce03b6255c"
    main(API_KEY_ID, API_KEY)
