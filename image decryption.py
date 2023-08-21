from PIL import Image
path=input("enter the absolute path of the image")
try: 
    img  = Image.open(path) 
except IOError:
    pass
key=int(input("Enter the key for decryption of image:"))
print("path of the file",path)
print("decryption key:",key)
fin=open(path,"rb")
image=fin.read()
fin.close()
image=bytearray(image)
for index, values in enumerate(image):
    image[index]=values ^ key
fin=open(path,"wb")
fin.write(image)
fin.close()
print("decription done")