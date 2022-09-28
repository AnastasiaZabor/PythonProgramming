# num = int(input())
#
# if 0 < num <= 13:
#     print("детство")
# else:
#     if 14 <= num <= 24:
#         print("молодость")
#     else:
#         if 25 <= num <= 59:
#             print("зрелость")
#         else:
#             print("старость")

a = int(input())
b = int(input())
c = int(input())

if a < b < c:
    print(b)
else:
    if b < a < c:
        print(a)
    else:
        if a < c < b:
            print(c)

