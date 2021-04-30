import sys
charindex = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shift = int(sys.argv[1])
result = ""
string = sys.stdin.readline()
for char in string:
  if char.isalpha() == True:
    num = charindex.index(char)
    if (num + shift) > 25:
      char = charindex[num+shift-25]
      result+= char
    else:
      char = charindex[num+shift]
      result += char
  else:
    result+= char
x = result.upper()
print(x)
