text_file = open('yellowpagemy-category.txt', 'r')
lines = text_file.readlines()
import string
for item in lines:
    seen = set()
    result = []
    printable = set(string.printable)
    asciiResult = filter(lambda x: x in printable, item)
    seen.add(asciiResult)
    result.append(asciiResult)
    print result
    with open('ascii.txt', 'a') as f:
        for x in result:
            f.write('{0}'.format(x))
