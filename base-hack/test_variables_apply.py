"""Set debugging vars to the build."""
set_variables = {
    "level_order_rando_on": 1,
    "level_order": [1, 5, 4, 0, 6, 2, 3],
    "troff_scoff_count": [100, 200, 300, 400, 410, 420, 430],
    "blocker_normal_count": [2, 3, 4, 5, 6, 7, 8],
    "key_flags": [0x4A, 0x8A, 0xA8, 0xEC, 0x124, 0x13D, 0x1A],
    "unlock_kongs": 0,
    "unlock_moves": 0,
    "fast_start_beginning": 1,
    "camera_unlocked": 0,
    "tag_anywhere": 1,
    "fast_start_helm": 0,
    "crown_door_open": 0,
    "coin_door_open": 0,
    "quality_of_life": 1,
}


def valtolst(val, size):
    """Convert the values to a list."""
    arr = []
    for x in range(size):
        arr.append(0)
    conv = val
    for x in range(size):
        if conv != 0:
            arr[size - x - 1] = int(conv % 256)
            conv = (conv - (conv % 256)) / 256
    return arr


def writeToROM(offset, value, size):
    """Write byte data to rom."""
    with open("rom/dk64-randomizer-base-dev.z64", "r+b") as rom:
        rom.seek(0x1FED020 + offset)
        rom.write(bytearray(valtolst(value, size)))


with open("include/variable_space_structs.h", "r") as varspace:
    varlines = varspace.readlines()
    struct_data = []
    for x in varlines:
        start = "ATTR_LINE"
        y = x.replace("\t", start)
        if y[:9] == start:
            struct_data.append(x.replace("\n", "").replace("\t", ""))
    struct_data2 = []
    for x in struct_data:
        location = x[3:8]
        other_info = x[12:].split(" ")
        other_data = [int(location, 16), "", "", 1]
        for y in range(len(other_info)):
            if y == (len(other_info) - 1):
                other_data[2] = other_info[y][:-1]
                count_split = other_data[2].split("[")
                if len(count_split) > 1:
                    other_data[2] = count_split[0]
                    other_data[3] = count_split[1].split("]")[0]
            else:
                other_data[1] += other_info[y] + " "
        other_data[1] = other_data[1][:-1]
        data_type = other_data[1]
        if "char" in data_type:
            other_data[1] = 1
        elif "short" in data_type:
            other_data[1] = 2
        elif "int" in data_type:
            other_data[1] = 4
        struct_data2.append(other_data)
    test_keys = set_variables.keys()
    for x in test_keys:
        for y in struct_data2:
            if x == y[2]:
                if type(set_variables[x]) is int:
                    if y[3] == 1:
                        writeToROM(y[0], set_variables[x], y[1])
                    # print(type(set_variables[x]))
                elif type(set_variables[x]) is list:
                    for z in range(min([int(y[3]), len(set_variables[x])])):
                        writeToROM(y[0] + (z * y[1]), set_variables[x][z], y[1])
                    # print(type(set_variables[x]))
    # print(struct_data2)