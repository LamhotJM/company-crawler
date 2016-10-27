def getUniqueItems(iterable):
    seen = set()
    result = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


text_file = open('xxxx.txt', 'r')
lines = text_file.readlines()

cleanListUrl = getUniqueItems(lines)
text_file.close()

for cleanUrl in cleanListUrl:
    with open('x2.txt', 'a') as f:
        f.write('{0}'.format(cleanUrl))
