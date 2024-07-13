import socket
import serial

def main():
    # Set up the serial connection
    serial_port = '/dev/ttyUSB0'  # Replace with your serial port
    baud_rate = 9600  # Replace with your baud rate
    ser = serial.Serial(serial_port, baud_rate)

    # Set up the socket server
    host = '127.0.0.1'  # Localhost
    port = 65432  # Port to listen on

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Received data: {data.decode()}")
                    
                    # Send the received data to the serial port
                    ser.write(data)
                    print(f"Sent data to serial port: {data.decode()}")

if __name__ == "__main__":
    main()
