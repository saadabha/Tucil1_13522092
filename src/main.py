import random


print("Selamat datang dalam permainan Breach Protocol")
print("Silahkan pilih masukan yang anda inginkan")
print("1. File .txt")
print("2. Masukkan manual")

pilih = int(input("=> "))
while pilih != 1 and pilih != 2:
    print("Masukkan salah")
    print("Silahkan pilih kembali")
    pilih = int(input("=> "))

if pilih == 1:
    filename = input("Masukkan nama file: ")
    file = open('load.txt','r')
    buffer_length = int(file.readline())
    content = file.readline()
    content = content.split()
    content = [int(num) for num in content]
    mwidth = content[0]
    mheight = content[1]
    matrix = [["" for i in range(mwidth)] for j in range(mheight)]
    for i in range(mheight):
        content = file.readline()
        content = content.split()
        content = [token for token in content]
        for j in range(mwidth):
            matrix[i][j] = content[j]
    content = int(file.readline())
    sequence_list = []
    for i in range(content):
        content = file.readline()
        templist = content.split()
        content = int(file.readline())
        sequence_list.append((content, templist))
    file.close()
else:
    token_count = int(input())
    token = input()
    token = token.split()
    buffer_length = int(input())
    content = input()
    content = content.split()
    content = [int(num) for num in content]
    mwidth = content[0]
    mheight = content[1]
    matrix = [["" for i in range(mwidth)] for j in range(mheight)]
    for i in range(mheight):
        for j in range(mwidth):
            elmt = random.choice(token)
            matrix[i][j] = elmt
    sequence_count = int(input())
    max_sequence = int(input())
    sequence_list = []
    for i in range(sequence_count):
        length = random.randint(2, max_sequence)
        sequence = []
        for j in range(length):
            sequence.append(random.choice(token))
        sequence_reward = random.randint(-100, 100)
        sequence_list.append((sequence_reward, sequence))

file = open('tes.txt','w')

def reward_count(sequence, buffer):
    reward = 0
    for i in range(len(sequence)):
        sub_list = sequence[i][1]
        if is_sublist(sub_list, buffer):
            reward += sequence[i][0]
    return reward

def is_sublist(sub_list, list):
    for i in range(len(list)-len(sub_list)+1):
        if list[i:i + len(sub_list)] == sub_list:
            return True
    return False

def is_elmt(sublist, koordinat):
    return sublist in koordinat

def add_buffer(currbuffer, koor, bool, templength):
    if bool:
        i = koor[len(koor)-1][0]
        for j in range(mheight):
            if j != koor[len(koor)-1][1] and not is_elmt([i, j], koor):
                currbuffer.append(matrix[i][j])
                koor.append([i, j])
                templength += 1
                bool = False
                reward = reward_count(sequence_list, currbuffer)
                file.write(str(reward)+' '+ str(currbuffer) + ' '+"\n")
                if templength < buffer_length:
                    add_buffer(currbuffer, koor, bool, templength)
                currbuffer.pop()
                koor.pop()
                templength -= 1
    else:
        j = koor[len(koor)-1][1]
        for i in range(mwidth):
            if i != koor[len(koor)-1][0] and not is_elmt([i, j], koor):
                currbuffer.append(matrix[i][j])
                koor.append([i, j])
                templength += 1
                bool = True
                reward = reward_count(sequence_list, currbuffer)
                file.write(str(reward)+' '+ str(currbuffer) + ' '+"\n")
                if templength < buffer_length:
                    add_buffer(currbuffer, koor, bool, templength)
                currbuffer.pop()
                koor.pop()
                templength -= 1

reward = 0
buffer = []
koordinat = []
if buffer_length != 0:
    for i in range(mwidth):
        buffertemp = []
        koordinattemp = []
        templength = 0
        buffertemp.append(matrix[0][i])
        koordinattemp.append([0, i])
        templength += 1
        reward = reward_count(sequence_list, buffertemp)
        file.write(str(reward)+' '+ str(buffertemp) + ' '+"\n")
        if buffer_length > 1:
            add_buffer(buffertemp, koordinattemp, False, templength)
    