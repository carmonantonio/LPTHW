from sys import argv

script, filename =argv

txt = open(filename)

print("Here is your file: %r" %filename)
print (txt.read())

print("type the file again:")
flie_again = input ("> ")

txt_again = open(flie_again)
print(txt_again.read())
