#1108 Defanging IP Address
address = "255.100.50.0"
def defanging(address):
    for ch in address:
        if ch=='.':
            ch.replace(".","[.]")
    return address
print(defanging(address))