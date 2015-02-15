__author__ = 'rafael'

import jsonrpclib

# Variables
ip = '50.242.94.227'
port = '8243'
username = 'eapi'
password = '99saturday'
url = 'https://{}:{}@{}:{}'.format(username, password, ip, port)
uri = '/command-api'
node = url+uri


def get_int_counter(interface, content, key):
    """Takes an interfaceID, content, & a key as arguments. Prints key value."""
    if 'interfaceCounters' in content and interface != 'Management1':
        counter_val = content['interfaceCounters'][key]
        print '{}: {} = {}'.format(interface, key, counter_val)
    else:
        pass


def get_interfaces(connection, command):
    """Takes an RPC object & a command as arguments.Returns interfaces in dic."""
    return connection.runCmds(1, [command])[0]['interfaces']


def get_connection(device):
    """Takes a url/uri as argument and returns a RPC connection object."""
    return jsonrpclib.Server(device)


def main():
    """ Calls get_connection, get_interfaces, and get_int_counters functions"""
    server = get_connection(node)
    interfaces = get_interfaces(server, 'show interfaces')
    for interface in sorted(interfaces):
        int_content = interfaces[interface]
        get_int_counter(interface, int_content, 'inOctets')
        get_int_counter(interface, int_content, 'outOctets')

if __name__ == "__main__":
    main()
