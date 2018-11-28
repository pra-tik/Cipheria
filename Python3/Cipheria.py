from tkinter import *
from tkinter.filedialog import askopenfilename
import pyAesCrypt

bufferSize = 64 * 1024

root = Tk()
v = StringVar()
def takefile():
				root.filename =askopenfilename()
				#root.filename.replace(" ", "")
def enc():
			print ("Encrypting")
			print (root.filename)
			d = v.get()
			k = len(d)
			if k >= 8 :
				print ("Encrypting ... ")
				pyAesCrypt.encryptFile(root.filename, root.filename+".aes",d, bufferSize)
				print ("Encryption Successful")

			else:
				print ("Please Enter key of lenght more than 8")
def dec():
		d = v.get()
		newfile = root.filename[:-4]
		k = len(d)
		if k >= 8 :
			print ("Decrypting ... ")
			print (root.filename)
			pyAesCrypt.decryptFile(root.filename,newfile, d , bufferSize)

			print ("Decryption Successful")

theLabel = Label(root, text="Welcome to Cipheria")
theLabel.pack()

B = Button(root, text ="Select File", command = takefile)

B.pack()


theLabel2 = Label(root,text="Enter Key")
theLabel2.pack()

E1 = Entry(root, bd =5,textvariable=v)
E1.pack()

B2 = Button(root,text="Encrypt", command = enc)
B2.pack(side = LEFT)

B3 = Button(root,text="Decrypt", command = dec)
B3.pack(side = RIGHT)

			
root.mainloop()
