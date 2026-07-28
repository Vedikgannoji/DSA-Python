items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"

def countItems(items,ruleKey,ruleValue):
    type=0
    color=1
    name=2
    count=0

    if ruleKey=="type":
        for i in items:
            if i[type]==ruleValue:
                count+=1
    elif ruleKey=="color":
        for i in items:
            if i[color]==ruleValue:
                count+=1
    else:
        for i in items:
            if i[name]==ruleValue:
                count+=1
    return count
print(countItems(items,ruleKey,ruleValue))
                
                