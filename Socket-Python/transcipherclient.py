import socket
import math

HOST='127.0.0.1'
PORT=12347

key = "HACK"
def encryptMessage(msg):
    cipher = ""
  
    
    k_indx = 0
  
    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
  
   
    col = len(key)
 
    row = int(math.ceil(msg_len / col))
  
    
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
  
   
    matrix = [msg_lst[i: i + col] 
              for i in range(0, len(msg_lst), col)]
  
    
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] 
                          for row in matrix])
        k_indx += 1
  
    return cipher
		
def main():
	sockett=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sockett.connect((HOST,PORT))
	
	while True:
		msg=input("Enter the plaintext : ")
		msg1=msg
		
		 
		
		
		postencoding=encryptMessage(msg)
		print("Ciphertext generated is : ",postencoding)
		msg=postencoding.encode("utf-8")
		sockett.send(msg)
		print("Message Sent!")
		
		
if __name__ == '__main__':
	main()
