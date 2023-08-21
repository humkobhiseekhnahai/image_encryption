from PIL import Image
path=input("enter the absolute path of the image")
try: 
    img  = Image.open(path) 
except IOError:
    pass
key = int(input("enter key for encryption of Image:"))
print("the path of file :",path)
print("key for encryption:",key)
fin = open(path,"rb")
image=fin.read()
fin.close()
image=bytearray(image)
for index, values in enumerate(image):
    image[index]=values ^ key
fin =open(path,"wb")
fin.write(image)
fin.close()
print("encryption done....")
