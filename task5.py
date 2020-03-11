#Hackerrank Two Strings
def twoStrings(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    if len(s1.intersection(s2)) == 0:
        return "NO"
    else:
        return "YES"
twoStrings()