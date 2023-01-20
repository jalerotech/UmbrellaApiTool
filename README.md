# Umbrella automation modules

## These are the main scripts created here so far:

- **CreateAuth.py**: The purpose of this script is to generate the access token that's used as a Bearer token for subsequent requests towards the umbrella deployment.

- **CreateNetwork.py**: This uses the access token from CreateAuth to create the network identity using the network data provided in the payload of the requst.

- **GetTunnels.py**: This fetches the data of the existing IPsec Tunnels on your deployment.

- **CreateTunnel.py**: This creates the tunnel on your deployment using the tunnel data supplied. 

- **RemoveTunnel.py**: This removed tunnel(s) on your deployment using the tunnel id (data type = list) supplied.

The file below contains the input data used when running the scripts above.

- **data_file.py** contains the API keys information and the payload data.

## How to use:

1. Clone the repository to your IDE.
2. Update the req_data_file.py file with your __API_KEY_NAME__ and __API_KEY__ from your org/deployment.
3. Update the tunnel.data dict on the req_data_file.py file in case you want to also create a tunnel using the script.
4. Run the CreateNetwork.py, GetTunnels.py or CreateTunnel.py script depending on your need.


## Note:

You must run CreateNetwork.py script from a device that's behind the public IP address you're trying to add as a Network Idwentity on your Umbrella deployment.
If not a warning would be displayed.
