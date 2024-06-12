from MultiOrgs.ListChildOrgs import returnChildOrgs
from Devices.roamingComputers import fetchRoamingComputers
from SWG.swgOverride import fetchOverrideSwgSetting, setOverrideSwgSetting
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
        # fetchRoamingComputers(API_KEY_ID, API_KEY, org)
        rc_list = fetchRoamingComputers(API_KEY_ID, API_KEY, org)
        writeToFile(file_path, rc_list)
        for rc in rc_list:
            resp = fetchOverrideSwgSetting(API_KEY_ID, API_KEY, rc, org)
            writeToFile(file_path, resp)
            # print(type(rc))
        # overrideSwgSetting(API_KEY_ID, API_KEY, origin_id, org_id)
        # Pauses the "returnUsers()" module for 5 seconds to not hit rate limiting.
        time.sleep(5)


if __name__ == '__main__':
    # API_KEY_ID = "Your_API_Key_Id"
    # API_KEY = "Your_API_Key"
    # # Lab API keys
    # API_KEY_ID = "44361325ceb24d9baf001d24bacfa24a"
    # API_KEY = "5de3d86d84fa4a9786039b71d0b4e2c4"
    # Lab MSP API creds (roaming clients only)
    API_KEY_ID = "deae3edd0bcf48059eb072725c3cf5be"
    API_KEY = "f82510d795a34eae8f0f7adf746b82e7"
    main(API_KEY_ID, API_KEY)
