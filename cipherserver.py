import socket
from string import ascii_lowercase

s = socket.socket()

PORT = 5500

s.bind(("", PORT))
s.listen(1)


def decode(cipher_text, key):
	alphabets = ascii_lowercase
	plain_text = ""
	for i in cipher_text:
		if i == " ":
			plain_text += " "
		else:
			plain_text += alphabets[((alphabets.index(i) - key) % 26)]
	return plain_text

while True:
	c, addr = s.accept()
	print('Got connection from', addr)

	data = c.recv(1024).decode()

	if not data:
		break

	cipher_text, key = data.split(";")
	plain_text = decode(cipher_text, int(key))

	print(f"Received Cipher Text: {cipher_text}")
	print(f"Received key: {key}")
	print(f"Decoded Text: {plain_text}")

	c.close()
