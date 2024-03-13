# file_name = "words.txt"
# with open(file_name, "r", encoding = "ulf-8") as file:
#     lst = set()
#     for word in file:
#         a = word.strip().split()
#             for i in a:
#                 c = i[-2:]
#                 if c.upper() == "ЕЯ":
#                     lst.add(c.upper())
#
#
#
# from pprint import pprint
#
# file_name = "words.txt"
# with open(file_name, "r", encoding="utf-8") as file:
#     lst = set()
#     for word in file:
#         a = word.strip()
#         if a.upper().strip()[-2:] == "ЕЯ":
#             lst.add(word.upper().strip())
# for i in sorted(lst, key=lambda x: (len(x), x)):
#     print(i)
#
#
# with open('words.txt', 'r', encoding='utf-8') as f:
#     lst = set()
#     for word in f:
#         qw = word.strip().split()
#         for i in qw:
#             qwe = i[-2:]
#             if "ЕЯ" == qwe.upper():
#                 lst.add(i.upper())
#
# for i in sorted(lst, key=lambda x: (len(x), x[0])):
#     print(i)
#
#
