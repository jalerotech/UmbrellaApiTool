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
