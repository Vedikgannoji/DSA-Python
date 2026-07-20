#Dictionary/Hashmaps
'''
student = {
    "name": "vedik",
    "age" : 19,
    "city": "Hyderabad"
}
print(student.get("name"))
print(student["age"])
student["college"]="MLRIT"
print(student)

student2=dict(name="abhinav",age="19",college="mlrit")
print(student2)
del student2["college"]
print(student2)

for key, value in student.items():
    print(f"{key} : {value}")
'''

#example-1 count frequency
s="abbacdde"
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for key,value in freq.items():
    print(f"{key}: {value}")

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
