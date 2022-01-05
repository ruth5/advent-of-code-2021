
def open_and_parse(filename):
    my_file = open(filename)
    i = 0
    parsed_list = []
    for line in my_file:
        stripped_line = list(line.rstrip())
        parsed_list.append(stripped_line)
        # i = i + 1
    parsed_list = list(map(int, parsed_list))
    return parsed_list

parsed_list = (open_and_parse('advent-input.txt'))
# print(parsed_list)
print(len(parsed_list))
print(len(parsed_list[0]))


# go through each row in list
low_points = []
for i in range(len(parsed_list)):
    #each element in that row
    for j in range(len(parsed_list[0])):
        element = int(parsed_list[i][j])
        # min_ = element
        min_ = 10
        if (i-1) > -1:
            up = int(parsed_list[i-1][j])
            min_ = min(min_, up)
        if (i + 1) < len(parsed_list):
            down = int(parsed_list[i+1][j])
            min_ = min(min_, down)
        if (j - 1) > -1:
            left = int(parsed_list[i][j-1])
            min_ = min(min_, left)
        if (j + 1) < len(parsed_list[0]):
            right = int(parsed_list[i][j+1])
            min_ = min(min_, right)
        # if min_ == element:
        if element < min_:
            low_points.append(element)
sum_ = 0
for point in low_points:
    sum_ += (point + 1)
print(sum_)



print(low_points)



