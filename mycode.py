import sys
charindex = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
shift = int(sys.argv[1])
result = ""
string = sys.argv[2]
string.lower()
for char in string:
  num = charindex.index(char)
  if char.isalpha() == True:
    elif (num + shift) > 25:
      result+= char
    else:
      char = charindex[num+shift]
      result += char
print(result)
