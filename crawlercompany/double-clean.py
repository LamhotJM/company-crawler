# def getUniqueItems(iterable):
#     seen = set()
#     result = []
#     for item in iterable:
#         if item not in seen:
#             seen.add(item)
#             result.append(item)
#     return result
#
#
# text_file = open('category.txt', 'r')
# lines = text_file.readlines()
#
# cleanListUrl = getUniqueItems(lines)
# text_file.close()
#
# for cleanUrl in cleanListUrl:
#     with open('clean.txt', 'a') as f:
#         f.write('{0}'.format(cleanUrl))
