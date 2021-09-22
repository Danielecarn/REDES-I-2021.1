from socket import * 

serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 6789 

serverSocket.bind(("localhost", serverPort)) 
serverSocket.listen(1)

while True: 
	print ('Pronto para receber conexões...')		
	connectionSocket, addr = serverSocket.accept() 
	print ('Conexão feita com ', addr, '\n')

	try:
		message =  connectionSocket.recv(1024)
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()
		connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")
 
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send(b"\r\n")
		connectionSocket.close()
	except IOError:
		connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
		connectionSocket.send(b"<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
		connectionSocket.close()

serverSocket.close()