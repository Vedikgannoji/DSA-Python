#49 Group Anagrams
strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    groups={}
    for word in strs:
        key="".join(sorted(word))
        if key in groups:
            groups[key].append(word)
        else:
            groups[key]=[word]
    return list(groups.values())

print(groupAnagrams(strs))