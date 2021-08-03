import socket

target_host = "0.0.0.0" #Change to www.google.com for original
target_port = 9998 # Change to port 80 for original

#Create socket object

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client

client.connect((target_host, target_port))

# Send some data

#client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

client.send(b'ABCDEF') # Send the test data to the tcpclient remove for original

# Receive some data

#response = client.recv(4096) # Remove comment for original

#print(response.decode()) # Remove comment for original
client.close()
