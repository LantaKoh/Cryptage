liste=['0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
message=str(input('Message à decoder : '))
cle=str(input('cle : '))
code=[]
li=len(cle)
b=0
c=0
res=[]
for x in range(len(message)):
	if c==li:
		c=0
	if message[x]==' ':
		res.append(' ')
	else:
		yo=liste.index(message[x])
		yi=liste.index(cle[c])
		nm=yo-yi
		if nm<0:
			nm=nm+26
		code.append(nm)
		b=b+1
		c=c+1
		res.append(liste[nm])
print(code)
ou=''.join(res)
print(ou)