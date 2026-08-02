#28 Index of the First Occurrence in a String

haystack = "sadbutsad"
needle = "sad"

def firstOccurance(haystack,needle):
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)]==needle:
            return i
    return -1
print(firstOccurance(haystack,needle))