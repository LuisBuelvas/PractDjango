import string
import random


fo = open("hola.txt", "wb")
fo.write("python Es el mejor lenguaje")
for i in range(10):
    texto = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
    fo.write("%s" % texto)
    
fo.close()

fo2 = open("hola.txt","r+")
srti = fo2.read()
print(srti)
fo2.close()