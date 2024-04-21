import jieba
import os
import re
# 读取停用词列表
def get_stopword_list(file):
    with open(file, 'r', encoding='utf-8') as f:    #
        stopword_list = [word.strip('\n') for word in f.readlines()]
    return stopword_list

# 分词 然后清除停用词语
def clean_stopword(str, stopword_list):
    result = ''
    chinese_pattern = re.compile('[\u4e00-\u9fff]+')  # 匹配汉字的正则表达式
    str = ''.join(chinese_pattern.findall(str))
    word_list = jieba.lcut(str)   # 分词后返回一个列表  jieba.cut(）   返回的是一个迭代器
    for w in word_list:
        if w not in stopword_list:
            result += ' '
            result+=w
    return result

if __name__ == '__main__':
    stopword_file = r"E:\informationsearch\tingyongci.txt"
    stopword_list = get_stopword_list(stopword_file)    # 获得停用词列表
    folder_path = r"E:\informationsearch\xmu_pages" # 替换为你的文件夹路径
    files = os.listdir(folder_path)
    os.chdir('E:\informationsearch\procxmu_pages')
    num =0
    for file_name in files:
        # 筛选出以'.txt'为扩展名的文件
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r',encoding='utf-8') as file:
                content = file.read()
                content = clean_stopword(content, stopword_list)
                os.chdir("E:\informationsearch\procxmu_pages")
                with open(file_name, 'w', encoding='utf_8') as f:
                    f.write(content)
