#open the file and allow you to read
f1 = open("demoText1.txt","r")
print(f1.read())
f1.close()
#overWrite the existing content
f2 = open("demoText1.txt","w")
f2.write("this message written by python Script")
f2.close()
#it adds new message without deleting old content
f3 = open("demoText1.txt","a")
f3.write("\n im appended by f3 object")
f3.close()
"""
1. ' r'  Read mode open file for Reading [ print(f1.read()) ]
2. ' w'  write mode open file for writing [f2.write("message) ]
3. ' a'  append mode open file for Reading 
"""