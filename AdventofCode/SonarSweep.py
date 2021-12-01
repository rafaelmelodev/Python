# i = [199,200,208,210,200,207,240,269,260,263]

# prev = i[0]
# count = 0

# for x in i:
#     if x > prev:
#         count += 1
#     prev = x

# print(count)

def SonarSweep_pt1 ():

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

    return count

print("Part 1 =", SonarSweep_pt1())

def SonarSweep_pt2():

    left_point = 0
    right_point = 2
    count = 0
    
    with open("input.txt", 'r') as f:
        values = list(map(lambda line: int(line), f.readlines()))
        previous = values[0] + values[1] + values[2]
        while right_point != len(values) - 1:
            new_window = previous - values[left_point] + values[right_point + 1]
            if new_window > previous:
                count += 1
            previous = new_window
            left_point += 1
            right_point += 1
    return count

print("Part 2 =", SonarSweep_pt2())