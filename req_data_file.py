api_key_data = {"API_KEY_ID": "905526a387aa45dbaee8ada7aa05d349", "API_KEY": "ad37c244a28543af956a8efc3782314a"}

payload_data = {
    "prefixLength": 32,
    "ipAddress": "91.177.228.223",
    "name": "tes network",
    "status": "OPEN",
    "isDynamic": True
}

tunnel_data = {
    "name": "Site01Tunnel",
    "siteOriginId": 123456,
    "serviceType": "SIG",
    "deviceType": "ASA",
    "networkCIDRs": [
        "123.111.222.25/24",
        "111.222.39.1/32"
    ],
    "transport": {"protocol": "IPSec"},
    "authentication": {
        "type": "PSK",
        "parameters": {
            "idPrefix": "prefix-string",
            "secret": "This123Secretlong"
        }
    }
}
