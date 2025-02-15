'''
    This file contains just a simple implementation of a socket-based
    distributed system written in MicroPython.
    @brief Make a Led Blink by sending remote messages
    
    This file contains the implementation of the Master of the
    Private WLAN
'''

import network
from machine import Pin
import socket
import json

SSID =              'pico-wlan'
PASSWORD =          'little-l-pico'
LEADER_LISTEN_PORT = 6060
LED_ON =             0
LED_OFF =            1
UNDEF_OPERATION =    2

led = Pin("LED", Pin.OUT)

def setup_wlan():
    nic = network.WLAN(network.WLAN.IF_AP)
    nic.config(essid=SSID, password=PASSWORD)
    nic.active(True)
    return nic

def is_connected(net):
    if not net.active():
        print('Some Errors Occured!')
        return False
    else:
        print('Connection OK!')
    return True

def parse_request(encoded_buffer):
    deser_data = json.loads(encoded_buffer)
    to_execute = deser_data['todo']
    if to_execute == LED_ON:
        return LED_ON
    else:
        return LED_OFF
    return UNDEF_OPERATION


def start_listening():
    # socket setup
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.bind(('', LEADER_LISTEN_PORT))
    conn.listen(1)
    
    while True:
        peer_conn, addr = conn.accept()
        print('Serve Request')
        buffer = peer_conn.recv(500)
        todo = parse_request(buffer)
        if todo is LED_ON:
            led.value(1)
            peer_conn.send('Led ON')
        elif todo is LED_OFF:
            led.value(0)
            peer_conn.send('Led OFF')
        else:
            peer_conn.send('What??')
        peer_conn.close()
    

nett = setup_wlan()
if is_connected(nett) == True:
    start_listening()
print('Stop!')

                
                


    
    
    





