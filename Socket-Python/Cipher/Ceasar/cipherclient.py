import socket 
from string import ascii_lowercase


s = socket.socket()	

PORT = 5500		

s.connect(("127.0.0.1", PORT))

def encode(plain_text, key):
	alphabets = ascii_lowercase
	cipher_text = ""
	for i in plain_text:
		if i == " ":
			cipher_text += " "
		else:
			cipher_text += alphabets[((alphabets.index(i) + key) % 26)]
	return cipher_text

def main():
	plain_text = input("Enter plain text: ")
	key = int(input("Enter key: "))

	#print(f"Entered plain text: {plain_text}")
	#print(f"Entered key: {key}")

	cipher_text = encode(plain_text, key)

	print(f"Cipher text sent: {cipher_text}")
	
	s.sendto(f"{cipher_text};{key}".encode(),('127.0.0.1', 5500))	
	s.close()

main()
