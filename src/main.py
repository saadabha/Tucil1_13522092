import random
import time


GREEN = "\033[32m"
END = "\033[0m"
print(f"""{GREEN}     
 _____         _                                       _         _____  _____  ______ ______
/  __ \       | |                                     | |       / __  \|  _  ||___  /|___  /
| /  \/ _   _ | |__    ___  _ __  _ __   _   _  _ __  | | __    `' / /'| |/' |   / /    / / 
| |    | | | || '_ \  / _ \| '__|| '_ \ | | | || '_ \ | |/ /      / /  |  /| |  / /    / /  
| \__/\| |_| || |_) ||  __/| |   | |_) || |_| || | | ||   <     ./ /___\ |_/ /./ /   ./ /   
 \____/ \__, ||_.__/  \___||_|   | .__/  \__,_||_| |_||_|\_\    \_____/ \___/ \_/    \_/    
         __/ |                   | |                                                        
        |___/                    |_|                                                        
______                           _         ______               _                        _  
| ___ \                         | |        | ___ \             | |                      | | 
| |_/ / _ __   ___   __ _   ___ | |__      | |_/ / _ __   ___  | |_   ___    ___   ___  | | 
| ___ \| '__| / _ \ / _` | / __|| '_ \     |  __/ | '__| / _ \ | __| / _ \  / __| / _ \ | | 
| |_/ /| |   |  __/| (_| || (__ | | | |    | |    | |   | (_) || |_ | (_) || (__ | (_) || | 
\____/ |_|    \___| \__,_| \___||_| |_|    \_|    |_|    \___/  \__| \___/  \___| \___/ |_|                                                                                                                                                                                         
{END}""")
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
    file = open('../test/'+filename,'r')
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
        if i > 0:
            for i in range(len(sequence_list)):
                listcheck = sequence_list[i][1]
                while listcheck == sequence:
                    sequence.pop()
                    sequence.append(random.choice(token))
        sequence_reward = random.randint(-100, 100)
        sequence_list.append((sequence_reward, sequence))
    print()
    print("Matrix")
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()
    print()
    print("Sequence")
    for i in range(len(sequence_list)):
        sekuens = sequence_list[i][1]
        for element in sekuens:
            print(element, end=" ")
        print()
        print(sequence_list[i][0])
    print()

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

def reward_check(rwrd, buff, koord):
    global reward, buffer, koordinat
    if rwrd >= reward:
        if rwrd == reward:
            if len(buff) < len(buffer):
                reward = rwrd
                buffer = buff.copy()
                koordinat = koord.copy()
        else:
            reward = rwrd
            buffer = buff.copy()
            koordinat = koord.copy()
    

def add_buffer(currbuffer, koor, bool, templength):
    if bool:
        i = koor[len(koor)-1][0]
        for j in range(mwidth):
            if j != koor[len(koor)-1][1] and not is_elmt([i, j], koor):
                currbuffer.append(matrix[i][j])
                koor.append([i, j])
                templength += 1
                bool = False
                reward = reward_count(sequence_list, currbuffer)
                reward_check(reward, currbuffer, koor)
                if templength < buffer_length:
                    add_buffer(currbuffer, koor, bool, templength)
                currbuffer.pop()
                koor.pop()
                templength -= 1
    else:
        j = koor[len(koor)-1][1]
        for i in range(mheight):
            if i != koor[len(koor)-1][0] and not is_elmt([i, j], koor):
                currbuffer.append(matrix[i][j])
                koor.append([i, j])
                templength += 1
                bool = True
                reward = reward_count(sequence_list, currbuffer)
                reward_check(reward, currbuffer, koor)
                if templength < buffer_length:
                    add_buffer(currbuffer, koor, bool, templength)
                currbuffer.pop()
                koor.pop()
                templength -= 1

reward = 0
buffer = []
koordinat = []
start = time.time()

if buffer_length != 0:
    for i in range(mwidth):
        buffertemp = []
        koordinattemp = []
        templength = 0
        buffertemp.append(matrix[0][i])
        koordinattemp.append([0, i])
        templength += 1
        rewardtemp = reward_count(sequence_list, buffertemp)
        if i == 0:
            reward = rewardtemp
            buffer = buffertemp.copy()
            koordinat = koordinattemp.copy()
        else:
            reward_check(rewardtemp, buffertemp, koordinattemp)
        if buffer_length > 1:
            add_buffer(buffertemp, koordinattemp, False, templength)
    print(reward)
    for element in buffer:
        print(element, end=' ')
    print()
    for i in range(len(koordinat)):
        print(koordinat[i][1]+1, end=", ")
        print(koordinat[i][0]+1)
    print()
else:
    print("Tidak ada solusi")
    print()

end = time.time()
print((end-start)*1000, end=" ms")
print()
save = input("Apakah ingin menyimpan solusi? (y/n) ")
save = save.lower()

if save == "y":
    filename = input("Masukkan nama file: ")
    file = open("../test/"+filename,"w")
    if buffer_length == 0:
        file.write("Tidak ada solusi\n")
    else:
        file.write(str(reward))
        file.write("\n")
        for element in buffer:
            file.write(str(element))
            file.write(" ")
        file.write("\n")
        for i in range(len(koordinat)):
            file.write(str(koordinat[i][1]+1))
            file.write(", ")
            file.write(str(koordinat[i][0]+1))
            file.write("\n")
        file.write("\n")
    file.write(str((end-start)*1000))
    file.write(" ms\n")    
    file.close()

    