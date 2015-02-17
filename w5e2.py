__author__ = 'rafael'

import argparse
import eapilib

eapi_params = {'username': 'eapi', 'password': '99saturday',
               'port': 8243, 'hostname': '50.242.94.227'}


def create_vlan(number, name=None):
    """Takes a VLAN ID and a VLAN name as arguments. If VLAN doesn't exists,
    creates the VLAN; otherwise, informs VLAN already exists."""
    if check_vlan(number):
        print 'VLAN {} is already exist.'.format(number)
    else:
        create_connection().config(['vlan '+number, 'name '+name])
        print 'VLAN {} {} created'.format(number, name)


def delete_vlan(number):
    """Takes a VLAN ID as argument and calls check_vlan to see VLAN exists.
    If VLAN exists deletes the VLAN; otherwise, informs VLAN doesn't exist """
    if check_vlan(number):
        create_connection().config(['no vlan '+number])
        print 'Deleted VLAN {}.'.format(number)
    else:
        print 'VLAN {} doesn\'t exists.'.format(number)


def create_connection():
    """Create an instance of create_connection & pass dictionary as parameters"""
    return eapilib.create_connection(**eapi_params)


def check_vlan(number):
    """Takes a VLAN ID as argument. Returns True if in database; False if not"""
    vlan_list = create_connection().run_commands(['show vlan'])[0]['vlans'].keys()
    return number in vlan_list
    
    
def display_vlans():
    """ Displays the content of the VLAN database."""
    vlans = create_connection().run_commands(['show vlan'])[0]['vlans']
    print'The VLAN database contains the following VLANS:'
    for key in vlans.keys():
        print 'VLAN ID: {} \tVLAN NAME: {}'.format(key, vlans[key]['name'])
    
    
def main():
    """Process arguments and calls delete_vlan or crete_vlan function."""
    parser = argparse.ArgumentParser()
    parser.add_argument("number", help="VLAN ID (Number)", action="store")
    parser.add_argument("--name", help="To specify a VLAN name", action="store", dest="name")
    parser.add_argument("--remove", help="Deletes the specified VLAN ID", action="store_true")
    args = parser.parse_args()
    number = args.number
    remove = args.remove
    name = args.name

    if remove:
        delete_vlan(number)
    elif 99 < int(number) < 999:
        create_vlan(number, name)
    else:
        print 'Bad input; try again.'

    display_vlans()

if __name__ == "__main__":
    main()
 
