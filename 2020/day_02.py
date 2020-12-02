class Password:
    def __init__(self, new_min, new_max, target, data):
        self.min    = new_min
        self.max    = new_max
        self.target = target
        self.data   = data

    def is_valid_one(self):
        return self.min <= self.data.count(self.target) <= self.max

    def is_valid_two(self):
        checksum = 0
        checksum += self.data[self.min - 1] == self.target
        checksum += self.data[self.max - 1] == self.target
        return checksum == 1

def get_formatted_pass(s):
    return int(s[0].split('-')[0]), int(s[0].split('-')[1]), \
        s[1][:-1], s[2]

file_data = []
with open('day_02_input', 'r') as f:
    for line in f:
        splitted = line.split()
        file_data.append(splitted)


print('PART ONE')
print('--------')

valid_count = 0
for s in file_data:
    p_list = get_formatted_pass(s)
    valid_count += Password(p_list[0], p_list[1], p_list[2], p_list[3]).is_valid_one()

print("solution is " + str(valid_count))

print('\n')
print('PART TWO')
print('--------')

valid_count = 0
for s in file_data:
    p_list = get_formatted_pass(s)
    valid_count += Password(p_list[0], p_list[1], p_list[2], p_list[3]).is_valid_two()

print("solution is " + str(valid_count))

