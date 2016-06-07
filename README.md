# godaddyDDNS
For those like me who have Domains registered with Godaddy, pointing to a home private lab. This little script allows you to dynamically update your A recors with you home public IP address.
The script is based of the python module Godaddypy written by Julian Coy.

# Required packages:
  - godaddypy
  - Json
  - request
# Usage
Get your key and secret key from the godaddy website. Add them to the config.json file
I run it as a cron Job on a Linux utility box
