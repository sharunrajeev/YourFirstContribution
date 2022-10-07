import socket
import math
  
key = "HACK"
IP = '127.0.0.1'
PORT = 12347

def decryptMessage(cipher):
    msg = ""
  
    # track key indices
    k_indx = 0
  
    # track msg indices
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
  
    
    col = len(key)
      
    
    row = int(math.ceil(msg_len / col))
  
    
    key_lst = sorted(list(key))
  
    
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
  
    
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
  
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
  
     
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")
  
    null_count = msg.count('_')
  
    if null_count > 0:
        return msg[: -null_count]
  
    return msg
def main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((IP, PORT))
	server.listen(10)
	while True:
		client, address = server.accept()
		print(f"Connected to {address[0]}  :{address[1]}")
		ds=client.recv(1024).decode("utf-8")
		print("Data received is {}".format(ds))

		 
		
		postdecoding=decryptMessage(ds)
		print("Plaintext after decoding is : ",postdecoding)
		
		
		
	
		
		
	
	

if __name__ == '__main__':
	main()
