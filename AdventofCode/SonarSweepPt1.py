# i = [199,200,208,210,200,207,240,269,260,263]

# prev = i[0]
# count = 0

# for x in i:
#     if x > prev:
#         count += 1
#     prev = x

# print(count)

with open("input.txt", 'r') as f:
    prev = None
    count = 0

    for l in f.readlines():
        if not prev:
             prev = int(l)
        else:
            if prev < int(l):
                count += 1
        prev = int(l)

print("Part 1 =", count)
