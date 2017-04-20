#Corey Kipp (ID: 57723335)
#Kevin Teer (ID: 27649116)

from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'localhost'

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver,25))
#Fill in end

recv = clientSocket.recv(1024)
print recv
if recv[:3] != '220':
    print '220 reply not received from server.'

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
    print '250 reply not received from server.'

# Send MAIL FROM command and print server response.
# Fill in start
mail_from = 'MAIL FROM: <kippc@uci.edu>\r\n'
clientSocket.send(mail_from)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not recieved from server.'
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcpt_to = 'RCPT TO: <kippc@uci.edu>\r\n'
clientSocket.send(rcpt_to)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not recieved from server.'

# Fill in end

# Send DATA command and print server response.
# Fill in start
data = 'Data\r\n'
clientSocket.send(data)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'
# Fill in end

# Send message data.
# Fill in start
clientSocket.send(msg + endmsg)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'
# Fill in end

# Message ends with a single period.
# Fill in start
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quit = 'Quit\r\n'
clientSocket.send(quit)
recv1 = clientSocket.recv(1024)
print recv1
if recv1[:3] != '250':
	print '250 reply not received from server.'
# Fill in end
