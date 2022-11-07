
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count=0
listOfEmails = []
for line in fhand:
    words = line.split()
    i = 0

    for word in words:
        if word == "From":
            count += 1
            listOfEmails.append(words[i+1])
        i+=1

listOfHostnames = []
for email in listOfEmails:
    index1 = email.index("@", 0)
    index2 = email.index(".", 0)
    listOfHostnames.append(email[index1+1:index2])

counts = dict()

for host in listOfHostnames:
     if host not in counts:
        counts[host] = 1
     else:
        counts[host] += 1

print("Ispis dictionarya ->",counts)
print("Ispis prvih 5 mailova->",listOfEmails[0:5])


