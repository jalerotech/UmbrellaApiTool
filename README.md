There are 3 main scripts created here so far:

1. CreateAuth.py:
   The purpose of this script is to generate the access token that's used as a Bearer token for subsequent requests towards the umbrella deployment.

2. CreateNetwork.py:
   This uses the access token from CreateAuth to create the network identity using the network data provided in the payload of the requst.

3. CreateTunnel.py:
   This creates the tunnel on your deployment using the tunnel data supplied.
   It runs a local script _get_site_origin_id that populates the "siteOriginId" field in the tunnel data file.
   This is required to create the tunnel on your deployment.

4. req_data_file.py contains the API keys information and the payload data.

How to use:

"""Instruction here"""
