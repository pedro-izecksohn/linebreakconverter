def unix2dos (b):
    ret = bytes()
    for c in b:
        if c==ord("\n"):
            ret+=bytes("\r\n", "utf-8")
        else:
            ret+=c.to_bytes(1,"little")
    return ret

def dos2unix (b):
    ret = bytes()
    for i,c in enumerate(b):
                if c!=ord("\r"):
                    ret+=c.to_bytes(1,"little")
                else:
                    if (i<(len(b)-1)) and (b[i+1]==ord("\n")):
                        continue
                    ret+=c.to_bytes(1,"little")
    return ret

ifn = input ("Enter the filename to convert: ")
ifile = open (ifn, "rb")
ib = ifile.read()
ifile.close()
answer = int(input("Enter 1 to convert from Unix to DOS\nor enter 2 to convert from DOS to Unix: "))
if answer==1:
    ob = unix2dos(ib)
elif answer==2:
    ob = dos2unix(ib)
else:
    print ("I did not understand your answer.")
    exit()
ofn = input ("Enter the filename to output: ")
ofile = open (ofn, "xb")
ofile.write(ob)
ofile.close()
print ("Success.")
