import requests
import json
import logging
from CreateAuth import get_access_token
from req_data_file import api_key_data, payload_data

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


# def create_network(data) -> str:
#     """
#     Creates the network identity on your org deployment using the network data provided
#     :param data: network data
#     :return:
#     """
#     access_token = get_access_token(api_key_data["API_KEY_ID"], api_key_data["API_KEY"])
#     # get_site_id(access_token)
#
#     logger = logging.getLogger('Running custom Umbrella create_network Script ')
#     logger.info('Creating network identity with the data provided: ')
#
#     url = "https://api.umbrella.com/deployments/v2/networks"
#
#     # Jsonify the dict for the request payload
#     json_dict = json.dumps(data, indent=4)
#     headers = {
#         "Content-Type": "application/json",
#         "Accept": "application/json",
#         "Authorization": f"Bearer {access_token}"
#     }
#
#     resp = requests.post(url, headers=headers, data=json_dict)
#
#     # Note ensure you're running this script from a device behind the public IP address used in the payload data.
#     resp_txt = resp.text
#     if "The ip address you provided is outside of your verified cidr blocks" == json.loads(resp_txt)['message']:
#         print(f"Your device is not behind the public IP {data['ipAddress']} "
#               f"you're trying to add as a network identity on Umbrella deployment.")
#     else:
#         print("Network identity created")
#
#     return resp_txt


def get_site_id():
    access_token = get_access_token(api_key_data["API_KEY_ID"], api_key_data["API_KEY"])
    url = "https://api.umbrella.com/deployments/v2/sites"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    resp = requests.get(url, headers=headers)
    # print(resp.text)
    return resp


if __name__ == "__main__":
    get_site_id()
    # create_network(payload_data)
