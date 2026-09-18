import requests

def send_message(message="Hello from sender!", url="http://<RASPBERRY_PI_IP>:5000/receive"):
    try:
        # Send the message as a POST request
        response = requests.post(url, data=message.encode('utf-8'))
        # Print the server's response
        print("Server response:", response.text)
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the Raspberry Pi. Is the server running?")

if __name__ == '__main__':
    send_message()