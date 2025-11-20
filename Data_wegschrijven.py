f = open("mijndat.txt","w")

f.write("\nDit is regel 1")
f.write("\nDit is regel 2")

f.close()

f = open("mijndta.txt","a")
f.write("\nDit is regel 3")
f.write("\nDit is regel 4")
f.close()

f = open("mijdata.txt","r")
inhoud = f.read()
print(inhoud)
f.close()