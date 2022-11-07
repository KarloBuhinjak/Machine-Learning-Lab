
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count=0
sum=0
for line in fhand:
    words = line.split()
    i = 0

    for word in words:
        if word == "X-DSPAM-Confidence:":
            count += 1
            sum += float(words[i+1])

        i+=1
print("Ime datoteke: ", fname)
print("Average X-DSPAM-Confidence: ", float(sum/count))
