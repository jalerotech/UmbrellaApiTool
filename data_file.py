# api_key_data = {"API_KEY_ID": "905526a387aa45dbaee8ada7aa05d349", "API_KEY": "ad37c244a28543af956a8efc3782314a"}
# api_key_data = {"API_KEY_ID": "5ac0e75359a546919a50aaca0dad0c43", "API_KEY": "623c173b4e4142329646cb2cfa15e803"}
# api_key_data = {"API_KEY_ID": "2893a77986cc4340a78733f077db2448", "API_KEY": "ed0ee232eae448ef9d610dce03b6255c"}

payload_data = {
    "prefixLength": 32,
    "ipAddress": "91.177.228.223",
    "name": "tes network",
    "status": "OPEN",
    "isDynamic": True
}

tunnel_data = {
    "name": "Site04Tunnel",
    "serviceType": "SIG",
    "deviceType": "ASA",
    "networkCIDRs": [
        "123.111.222.2/24",
        "111.222.39.8/32"
    ],
    "transport": {"protocol": "IPSec"},
    "authentication": {
        "type": "PSK",
        "parameters": {
            "idPrefix": "prefix-string4",
            "secret": "Thisisthe16orlongersecret"
        }
    }
}
