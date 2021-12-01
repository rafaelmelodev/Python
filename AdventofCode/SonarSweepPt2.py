init_value = 0
end_value = 2
count = 0
    
with open("input.txt", 'r') as f:
    # Mapping values into an integer list
    val = list(map(lambda line: int(line), f.readlines()))
    # First window
    prev = val[0] + val[1] + val[2]

    while end_value != len(val) - 1:
        #
        new_window = prev - val[init_value] + val[end_value + 1]
        if new_window > prev:
            count += 1
        prev = new_window
        init_value += 1
        end_value += 1

print("Part 2 =", count)