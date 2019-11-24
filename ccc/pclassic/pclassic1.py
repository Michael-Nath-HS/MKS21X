def a(s):
    longestString = ""
    runningString = s[0]
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            runningString += s[i]
        else:
            if len(runningString) > len(longestString):
                longestString = runningString
            runningString = s[i]
    return longestString


print(a("aaabbbaaaabbb"))
print(a("bbbbbaaaaab"))
