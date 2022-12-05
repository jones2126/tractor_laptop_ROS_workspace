import socket
try:
    socket.create_connection(('8.8.8.8',80))
    print 'connected to google'
except socket.error as msg:
    print 'there is no connection'