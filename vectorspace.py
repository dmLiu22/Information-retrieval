import sys,os
# 导入图形组件库
import math
import heapq
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor
#导入做好的界面库
from untitledVSModel import Ui_MainWindow

N = 8000
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        #初始化界面组件
        self.setupUi(self)
        #and
        self.pushButton.clicked.connect(self.andFunc)
        #or
        self.pushButton_2.clicked.connect(self.orFunc)
        #not
        self.pushButton_3.clicked.connect(self.notFunc)
        #计算
        self.pushButton_4.clicked.connect(self.cal)
    def andFunc(self):
        tp = self.lineEdit.text() + " and "
        self.lineEdit.setText(tp)
        self.lineEdit.setFocus()
    def orFunc(self):
        tp = self.lineEdit.text() + " or "
        self.lineEdit.setText(tp)
        self.lineEdit.setFocus()
    def notFunc(self):
        tp = self.lineEdit.text() + " not "
        self.lineEdit.setText(tp)
        self.lineEdit.setFocus()
    def cal(self):
        if self.lineEdit.text():
          try:
            # 建立列表
            my_list = []
            for line in content:
                my_list.append(line.strip())
            def sort_key(word):
                return inverted_index[word][0]

            def And(list1, list2):
                i, j = 0, 0
                res = []
                while i < len(list1) and j < len(list2):
                    if list1[i] == list2[j]:
                        res.append(list1[i])
                        i += 1
                        j += 1
                    elif list1[i] < list2[j]:
                        i += 1
                    else:
                        j += 1
                return res

            def Or(list1, list2):
                i, j = 0, 0
                res = []
                while i < len(list1) and j < len(list2):
                    # 同时出现，只需要加入一次
                    if list1[i] == list2[j]:
                        res.append(list1[i])
                        i += 1
                        j += 1
                    # 指向较小数的指针后移，并加入列表
                    elif list1[i] < list2[j]:
                        res.append(list1[i])
                        i += 1
                    else:
                        res.append(list2[j])
                        j += 1
                # 加入未遍历到的index
                res.extend(list1[i:]) if j == len(list2) else res.extend(list2[j:])
                return res

            def calculate_tfidf(tf, idf):
                return (1 + math.log(tf)) * idf

            # 计算两个向量的点积
            def dot_product(vec1, vec2):
                return sum(vec1[word] * vec2[word] for word in vec1)

            def AndNot(list1, list2):
                return list(set(list1) - set(list2))

            def orNot(list1, list2):
                return list(set(list1) | (set(str(x) for x in range(8000)) - set(list2)))

            def my_not(lis):
                return list(set(str(x) for x in range(8000)) - set(lis))
            # 计算向量的大小
            def magnitude(vec):
                return math.sqrt(sum(vec[word] ** 2 for word in vec))

            # 计算两个向量的余弦相似度
            def cosine_similarity(vec1, vec2):
                dot = dot_product(vec1, vec2)
                mag1 = magnitude(vec1)
                mag2 = magnitude(vec2)
                if mag1 == 0 or mag2 == 0:
                    return 0.0
                #return dot / (mag1 * mag2)
                return dot

            # 输入查询词语和选项
            query = self.lineEdit.text()
            paichuname = []
            if 'and' in query:
                namecpoy = []
                query = query.split(' and ')
                for word in query:
                    if 'not' not in word:
                        namecpoy.append(word)
                    else:
                        paichuname.append(word[5:])
                query = []
                query.extend(namecpoy)

            # 使用优先队列存储文档列表
                priority_queue = []
                while len(query) > 0:
                    word = query.pop(0)
                    sorted_list = sorted(inverted_index[word][1].keys())
                    heapq.heappush(priority_queue, sorted_list)

            # 通过求交集的方式获取包含所有查询词语的文档
                while len(priority_queue) > 1:
                    list1 = heapq.heappop(priority_queue)
                    list2 = heapq.heappop(priority_queue)
                    result_docs = And(list1, list2)
                    sorted_list = sorted(result_docs)
                    heapq.heappush(priority_queue, sorted_list)
            # 得到包含所有查询词语的文档列表
                result_docs = priority_queue.pop(0)

                for x in paichuname:
                    result_docs = AndNot(result_docs,inverted_index[x][1].keys())
            else:
                query = query.split(' or ')
                namecpoy = []
                namecpoy.extend(query)
                # 使用优先队列存储文档列表
                priority_queue = []
                while len(query) > 0:
                        word = query.pop(0)
                        sorted_list = sorted(inverted_index[word][1].keys())
                        heapq.heappush(priority_queue, sorted_list)

                # 通过求交集的方式获取包含所有查询词语的文档
                while len(priority_queue) > 1:
                        list1 = heapq.heappop(priority_queue)
                        list2 = heapq.heappop(priority_queue)
                        result_docs = Or(list1, list2)
                        sorted_list = sorted(result_docs)
                        heapq.heappush(priority_queue, sorted_list)
                # 得到包含所有查询词语的文档列表
                result_docs = priority_queue.pop(0)
            word_list = []
            doc_lengths = {}


            # 打开文件并读取内容
            for doc_id in result_docs:
                list3 = revindex[doc_id]
                word_list.extend(list3)

            doc_tfidf = {}
            for doc_id in result_docs:
                doc_tfidf[doc_id] = {}
                for word in word_list:
                    doc_counts = inverted_index[word]
                    if doc_counts is not None and str(doc_id) in doc_counts[1]:
                        tf = doc_counts[1][str(doc_id)]
                        idf = math.log(N / doc_counts[0])
                        tfidf = calculate_tfidf(tf, idf)
                        doc_tfidf[doc_id][word] = tfidf
                    else:
                        doc_tfidf[doc_id][word] = 0.0
            quevec = {}
            for word in word_list:
                if word in namecpoy:
                    doc_counts = inverted_index[word]
                    tf = 1
                    idf = math.log(N / doc_counts[0])
                    tfidf = idf
                    quevec[word] = tfidf
                else:
                    quevec[word] = 0.0
            # 对 quevec 进行归一化处理
            quevec_length = math.sqrt(sum(value ** 2 for value in quevec.values()))  # 计算 quevec 的长度
            for word in quevec:
                quevec[word] /= quevec_length
            similarities = {}
            for doc_id in result_docs:
                doc_vector = doc_tfidf[doc_id]
                doc_length = math.sqrt(sum(value ** 2 for value in doc_vector.values()))  # 计算文档向量的长度
                for word in doc_vector:
                    doc_vector[word] /= doc_length

                doc_tfidf[doc_id] = doc_vector
                similarity = cosine_similarity(quevec, doc_vector)
                similarities[doc_id] = similarity
            # 按相似度从高到低排序文档编号
            sorted_docs = sorted(similarities, key=similarities.get, reverse=True)
            self.textEdit.clear()
            # 打印结果列表中的文档内容
            ord = 0
            le = '共有' + str(len(sorted_docs)) + "个相关网站"
            highlighted_text = '<span style="background-color: yellow;">' + le + '</span>'
            self.textEdit.append(highlighted_text)
            for doc_id in sorted_docs:
                ord +=1
                if ord <=10:
                    start_color = QColor(255, 255, 0)  # Yellow
                    end_color = QColor(255, 0, 0)  # Red

                    # Calculate the color gradient steps
                    gradient_steps = 10  # Number of gradient steps
                    red_step = (end_color.red() - start_color.red()) / gradient_steps
                    green_step = (end_color.green() - start_color.green()) / gradient_steps
                    blue_step = (end_color.blue() - start_color.blue()) / gradient_steps
                    text = my_list[int(doc_id)]
                    red = int(start_color.red() + (red_step * ord))
                    green = int(start_color.green() + (green_step * ord))
                    blue = int(start_color.blue() + (blue_step * ord))
                    color = QColor(red, green, blue)

                    # Set the gradient color to the text
                    text = f"<span style='background-color: {color.name()};'>{text}</span>"
                    self.textEdit.append(text)
                else:
                    self.textEdit.append(my_list[int(doc_id)])
          except Exception as e:
              QMessageBox.warning(self, "警告", "语法错误", QMessageBox.Yes)
        else:
            QMessageBox.warning(self,"警告","空值",QMessageBox.Yes)

if __name__ == "__main__":
    with open("daopaisuoyin.txt", 'r', encoding='utf-8') as file:
        content = file.read()
    inverted_index = eval(content)
    with open("dictionary2.txt", 'r', encoding='utf-8') as file:
        content = file.read()
    revindex = eval(content)
    # 打开文件并读取内容
    file_path = r"lianjie.txt"  # 文件路径
    with open(file_path, 'r') as file:
        content = file.readlines()
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    #创建QApplication 固定写法
    app = QApplication(sys.argv)
    # 实例化界面
    window = MainWindow()
    #显示界面
    window.show()
    #阻塞，固定写法
    sys.exit(app.exec_())
