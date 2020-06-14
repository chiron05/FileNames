filename =str(input("Input the Filename:"))
z= filename.split(".")
if(z[1]=="py"):
    print("The extension of the file is: 'python'")
elif(z[1]=="c"):
    print("The extension of the file is: 'c'")
elif(z[1]=="c++"):
    print("The extension of the file is: 'c++'")
elif(z[1]=="java"):
    print("The extension of the file is: 'java'")
else:
    print("Please add extension to the file")