import socket
import time 	#Current time
import sys		#For exit

class Falcon:
	#Class describing Simple HTTP server object

	def __init__(self):
		#Constructor	
		self.host=''
		self.port=8080

	def activate(self):
		#Aquire the socket
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		print "Establishing Conection on port :",self.port
		
		self.socket.bind((self.host,self.port))
		while True:
			try:
				self.connection()
			except KeyboardInterrupt:
				print "Shutting down the web server"
				sys.exit(1)

	def headers(self):
		#Generates HTTP response Headers

		self.head=''
		self.head += "HTTP/1.1 200 OK\n"
		self.head += "status: 200 OK\n"
		self.head += "version: HTTP/1.1\n"
		
		#Show current time in response headers
		current_time=time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
		
		self.head += "Date :" + current_time+"\n"

		self.head += "Server : Python HTTP Server\n"

		return self.head

	def connection(self):
		#Create the connection
		self.socket.listen(1)	#Maximum number of queued connections	
		
		conn,addr=self.socket.accept()
		# conn - socket to client
		# addr - clients address

		print("Connected to",addr)

		#Define response headers and response content
		response_headers=self.headers()
		
		#Open the html file and stores is contents into the variable response_content
		filename=open("index.html")
		response_content=filename.read()
		
		conn.send(response_headers)
		conn.send("\n")		#Response headers ans response content seperated by a new line
		conn.send(response_content)


#Starting point of execution
print "Falcon is starting"
s=Falcon()	#Contructing TheServer object
s.activate()	#Aquire the socket
