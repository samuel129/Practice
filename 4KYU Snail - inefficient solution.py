#order = right down left up
finalAns = []

snail_map = [[1,2,3],
         [8,9,4],
         [7,6,5]]

length = 0
for arr in snail_map:
    length += len(arr)

used_num = []
index = [0, 0]
#given an index, traverse through left and right of the row [up][left]
def right(index, snailmap):
    while True:
        if index in used_num:
            index[1] -= 1
            index[0] += 1
            return
        if snailmap[index[0]][index[1]] == snailmap[index[0]][-1]:
            return
        used_num.append([index[0],index[1]])
        index[1] += 1

def down(index, snailmap):
    while True:
        if index in used_num:
            index[0] -= 1
            index[1] -= 1
            return
        if snailmap[index[0]][index[1]] == snailmap[-1][-1]:
            return
        used_num.append([index[0],index[1]])
        index[0] += 1

def left(index, snailmap):
    while True:
        if index in used_num:
            index[1] += 1
            index[0] -= 1
            return
        if snailmap[index[0]][index[1]] == snailmap[-1][0]:
            return
        used_num.append([index[0],index[1]])
        index[1] -= 1

def up(index, snailmap):
    while True:
        if index in used_num:
            index[0] += 1
            index[1] += 1
            return
        if snailmap[index[0]][index[1]] == snailmap[0][0]:
            return
        used_num.append([index[0],index[1]])
        index[0] -= 1

def snail(snail_map):
    while len(used_num) < length:
        right(index, snail_map)
        down(index, snail_map)
        left(index, snail_map)
        up(index, snail_map)
    for arr in used_num:
        finalAns.append(snail_map[arr[0]][arr[1]])
    return finalAns

print(snail(snail_map))