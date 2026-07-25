#Boats to Save People (LeetCode 881)
people = [1,2,3,4]
limit = 5

def boats_to_save_people(people,limit):
    people.sort()
    left=0
    right=len(people)-1
    boats=0
    while left<=right:
        if people[left]+people[right]<=limit:
            left+=1
            right-=1
            boats+=1
        else:
            right-=1
            boats+=1
    return boats

            
    
print(boats_to_save_people(people,limit))

