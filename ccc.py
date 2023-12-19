import pickle
import os

rootDir = './data/mc/train'
with open(os.path.join(rootDir, 'train.pkl'), 'rb') as handle:
    data = pickle.load(handle)

spk_vec_list = []
for i in range(10):
    aa = []
    spk_name = data[i][0]
    aa.append(spk_name)
    spk_vec = data[i][1]
    aa.append(spk_vec)
    spk_vec_list.append(aa)

# print(spk_vec_list)

list = []
speakers = ['p262', 'p272', 'p229', 'p232', 'p292', 'p293', 'p360', 'p361', 'p248', 'p251']
for a in speakers:
    for i in range(len(speakers)):
        if(speakers[i] == a):
            list.append(spk_vec_list[i][1])

print(list)



