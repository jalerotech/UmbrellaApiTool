import requests
import logging
from Auth.CreateAuth import get_access_token
import json
from datetime import time
import time

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


def fetchRoamingComputers(API_KEY_ID, API_KEY, org_id) -> dict:
    logger = logging.getLogger('Running fetchRoamingComputers')
    access_token, org_id_ret = get_access_token(API_KEY_ID, API_KEY, org_id)
    url = "https://api.umbrella.com/deployments/v2/roamingcomputers"

    payload = None

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.request('GET', url, headers=headers, data=payload)
    device_per_originId = {}
    for rc in response.json():
        device_per_originId[rc['originId']] = []
        data = {'device-id': rc['deviceId'],
                'RC-version': rc['version'],
                'os-version': rc['osVersion'],
                'os-name': rc['osVersionName'],
                'org_id': org_id_ret
                }
        device_per_originId[rc['originId']].append(data)
        logger.info(f"Returning 'device_per_originId' list.")
    return device_per_originId


if __name__ == '__main__':
    # Lab API keys
    # API_KEY_ID = "44361325ceb24d9baf001d24bacfa24a"
    # API_KEY = "5de3d86d84fa4a9786039b71d0b4e2c4"
    # # JaleroHome org keys
    # API_KEY_ID = "3a74c8c3bde24c54addffd2f204c6d19"
    # API_KEY = "6bf04ea9b76c475f8c426be08427b739"
    # Lab MSP API creds
    API_KEY_ID = "deae3edd0bcf48059eb072725c3cf5be"
    API_KEY = "f82510d795a34eae8f0f7adf746b82e7"
    fetchRoamingComputers(API_KEY_ID, API_KEY, org_id=8245496)
