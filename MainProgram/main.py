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
        rc_list, list_of_originId = fetchRoamingComputers(API_KEY_ID, API_KEY, child_org_list)
        if rc_list:
            writeToFile(file_path, rc_list)
            if list_of_originId:
                for org_data in list_of_originId:
                    pass
                    # print(org_data)
                    # resp = fetchOverrideSwgSetting(API_KEY_ID, API_KEY, org_data)
                    # resp = fetchOverrideSwgSetting(API_KEY_ID, API_KEY, list_of_originId, child_org_list)
                    # writeToFile(file_path, resp)
    for org in child_org_list:
        data = returnUsers(API_KEY_ID, API_KEY, org)
        # writeToFile(file_path, data)
        # fetchRoamingComputers(API_KEY_ID, API_KEY, org)
        # rc_list, list_of_originId = fetchRoamingComputers(API_KEY_ID, API_KEY, org)
        # if rc_list:
        #     writeToFile(file_path, rc_list)
        # list_of_originIds = []
        # if rc_list:
            # co_data['ListOfDevice'].append(rc_list['ListOfDevice'][0])
            # print(f"rc_list -> {rc_list}")
            # for rc in rc_list['ListOfDevice']:
                # list_of_originIds.append(rc['originId'])
        # if rc_list:
        #     if list_of_originId:
                # resp = fetchOverrideSwgSetting(API_KEY_ID, API_KEY, list_of_originId, org)
                # writeToFile(file_path, resp)
        # Pauses the "returnUsers()" module for 5 seconds to not hit rate limiting.
    # print(f"co_data => {co_data}")
    time.sleep(5)


if __name__ == '__main__':
    # # Lab MSP API creds (roaming clients only)
    # API_KEY_ID = "deae3edd0bcf48059eb072725c3cf5be"
    # API_KEY = "f82510d795a34eae8f0f7adf746b82e7"
    # SANTANDER keys:
    API_KEY_ID = '2893a77986cc4340a78733f077db2448'
    API_KEY = 'ed0ee232eae448ef9d610dce03b6255c'
    main(API_KEY_ID, API_KEY)
