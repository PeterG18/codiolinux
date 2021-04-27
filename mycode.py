charindex = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
def encode(string, shift):
  string.lower()
  result = ""
  for char in string:
    num = charindex.index(char)
    if char == " ":
      result+= char
    elif (num + shift) > 25:
      result+= char
    else:
      char = charindex[num+shift]
      result += char
    return print(result)
