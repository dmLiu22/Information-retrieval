import os
import json
def preprocess_text(text):
    return text
import os

def build_inverted_index(folder_path):
    inverted_index = {}
    file_list = os.listdir(folder_path)
    for i in range(len(file_list)):
        file_path = os.path.join(folder_path, file_list[i])  # 获取文件的完整路径
        with open(r"E:\informationsearch\procxmu_pages/"+str(i)+'.txt', 'r', encoding='utf-8') as f:
            tt = f.read()
        words = tt.split()
        positions = {}
        for index, word in enumerate(words):
            if word not in inverted_index:
                inverted_index[word] = {}

            if i not in inverted_index[word]:
                inverted_index[word][i] = {
                    'tf': 1,
                    'positions': [index]
                }
            else:
                inverted_index[word][i]['tf'] += 1
                inverted_index[word][i]['positions'].append(index)
    return inverted_index

filename = r"E:\informationsearch\procxmu_pages"
di={}
# 构建倒排索引和统计词频
inverted_index = build_inverted_index(filename)
# 打印倒排索引和词频统计
for word, doc_counts in inverted_index.items():
    s=[len(doc_counts),doc_counts]
    di[word]=s
print(di)
di = dict(sorted(di.items(), key=lambda x: x[1][0]))
with open("E:\informationsearch\daopaisuoyinweizhi.txt", 'w',encoding='utf-8') as file:
    json.dump(di, file,ensure_ascii=False)

