from godaddypy import Client, Account
import json
import requests
__author__ = 'paul.sidze'


with open("config.json") as config_file:
    config = json.load(config_file)

def main():
    r = requests.get(config["public_ip"])
    current_ip = r.json()["ip"]
    my_acct = Account(api_key=config["key"], api_secret=config['secret'])
    client = Client(my_acct)
    my_domains = client.get_domains()
    daddy_ip = client.get_a_records(my_domains[0])[0]['data']
    if current_ip != daddy_ip:
        client.update_ip(current_ip, domains=[my_domains[0]])
    else:
        print "Your Public IP is %s and GoDaddy A record is %s for the domain %s" % (current_ip,daddy_ip, my_domains[0])
if __name__ == '__main__':
    main()