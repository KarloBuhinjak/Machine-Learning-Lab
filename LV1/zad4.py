
listaBrojeva = []
i=0
while True:
    broj = input("Unesite broj: ")

    if (broj == "done"):
        break

    listaBrojeva.append(broj)
total = 0
for ele in range(0, len(listaBrojeva)):
    total = total + int(listaBrojeva[ele])



print("Broj unešenih brojeva je ", len(listaBrojeva))
print("MAX:", max(listaBrojeva))
print("MIN:", min(listaBrojeva))
print("AVG:", float(total/len(listaBrojeva)))