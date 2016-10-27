text_file = open('test_case.txt', 'r')
lines = text_file.readlines()

import re

def removal(dirtyString):
    rep = {"['": "", "']": ""}
    rep = dict((re.escape(k), v) for k, v in rep.iteritems())
    pattern = re.compile("|".join(rep.keys()))
    bufferVar= pattern.sub(lambda m: rep[re.escape(m.group(0))], dirtyString[0])
    return bufferVar


for item in lines:
    seen = set()
    result = []

    if item.count(';') == 3:
        seen.add(item)
        result.append(item)
        print result
        with open('unity.txt', 'a') as f:
            for x in result:
                f.write('{0}'.format(x))


    else:
        s = ""
        s += item
        if s.count(';') == 3:
            result.append(s)
            with open('unity.txt', 'a') as f:
                for x in result:
                    f.write('{0}'.format(x))
