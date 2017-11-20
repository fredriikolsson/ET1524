import socket

serverName = "www.ingonline.nu"
serverPort = 80


# create TCP socket on client to use for connecting to remote server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((serverName, serverPort))
request = ("GET /tictactoe/index.php?board=xoxoeoexx HTTP/1.1\nHost: www.ingonline.nu\n\n")
# open the TCP connection
s.send(request)

resp = s.recv(1024)
print ("Response: ", resp)


s.close()

print ("\nDone")
