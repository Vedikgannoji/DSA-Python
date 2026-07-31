#1108 Defanging IP Address
address = "255.100.50.0"
def defanging(address):
    new=""
    for ch in address:
        if ch!='.':
            new=new+ch
        else:
            new=new+"[.]"
    return new
print(defanging(address))