import socket
import time

# ESP32 server details
ESP32_IP = "192.168.132.181"  # Replace with the actual IP address of the ESP32
ESP32_PORT = 10000

# Function to connect to ESP32 server
def connect_to_esp32(ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))
    return client_socket

def output():
    try:
        client_socket = connect_to_esp32(ESP32_IP, ESP32_PORT)
        print("Connected to ESP32")
        time.sleep(1)

        while True:
            # Receive data from ESP32
            data = client_socket.recv(1024).decode('utf-8')
            if data:
                print(f"Received: {data}")

                # Send '#' to reset the sequence if needed
                if data.strip() == "A" or data.strip() == "B":
                    print("Sending reset command to ESP32")
                    time.sleep(1)
                    client_socket.send('#'.encode('utf-8'))
                    break
                    
            # return data
            # break
        return data.strip()
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()
        print("Connection closed")

    # client_socket.close()
    print("Connection closed")
    return data.strip()

if __name__ == "__main__":
    output()
