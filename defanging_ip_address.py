#1108 Defanging IP Address
address = "255.100.50.0"
def defanging(address):
    new=""
    for ch in address:
        new+="[.]" if ch=="." else ch
    return new
print(defanging(address))