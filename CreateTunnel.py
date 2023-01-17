import requests
import json
import logging
from CreateAuth import get_access_token
from req_data_file import api_key_data, tunnel_data


def create_tunnel(data) -> str:
    """
    Creates a Tunnel on your org deployment using the data provided
    :param data: tunnel data
    :return:
    """
    access_token = get_access_token(api_key_data["API_KEY_ID"], api_key_data["API_KEY"])
    url = "https://api.umbrella.com/deployments/v2/tunnels"

    json_dict = json.dumps(data, indent=4)

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {access_token}"
    }

    resp = requests.post(url, headers=headers, data=json_dict)

    # Note ensure you're running this script from a device behind the public IP address used in the payload data.
    resp_txt = resp.text
    print(resp_txt)

    return resp_txt


if __name__ == "__main__":
    create_tunnel(tunnel_data)
