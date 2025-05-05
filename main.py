import subprocess

def get_vpn_status():
    try:
        status_bytes = subprocess.check_output("windscribe-cli status", shell=True)
        return status_bytes.decode('utf-8').strip()
    except subprocess.CalledProcessError:
        print("Error: Could not retrieve VPN status. Make sure if windscribe is installed you fucking moron.")
        return None

def print_vpn_status(status_str):
    if status_str:
        for line in status_str.split('\n'):
            line = line.strip()
            if line:
                if ':' in line:
                    key, value = line.split(':', 1)
                    print(f"{key.strip():15}: {value.strip()}")
                else:
                    print(line)

def check_connected():
    status = get_vpn_status()
    if status and "Disconnected" not in status:
        return True
    return False

def main():
    print("=====================")  
    connected = check_connected()
    if connected:
        print("You are connected. The feds can not see you, therefore you are now above the law")
    else:
        print("YOU ARENT CONNECTED!!!")
        print("WEE WOO THE FEDS CAN SEE YOU! DONT TORRENT ANYTHING!")
    print("=====================")
    status = get_vpn_status()
    print_vpn_status(status)
    print("=====================")

if __name__ == "__main__":
    main()
