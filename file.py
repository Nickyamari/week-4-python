f = open ('text', 'r')
print(f)

f.close()

# write data

f = open('text', 'w')
f.write("This is the new line.\n")
f.close()

# append data

f = open('text', 'a')
f.write("This is the additional line.\n")
f.close()

# read data

f = open('text', 'r')
print(f.readlines(), end="")
f.close()
