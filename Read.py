#file output.py
f = open('Test.txt', 'r')
#f.seek(2)
message = f.read()
print(message)
f.close
