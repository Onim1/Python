def strcomparagom(str):
    startIndex = 0
    endIndex = len(str) - 1

    for x in str:
        if str[startIndex] != str[endIndex]:
            return True
    return False

print(strcomparagom("lina"))