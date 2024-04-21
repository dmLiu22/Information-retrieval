import sys,os
# 导入图形组件库
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import jieba
#导入做好的界面库
from untitledlocationplus import Ui_MainWindow
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        #初始化界面组件
        self.setupUi(self)
        self.pushButton.clicked.connect(self.andFunc)
        #or
        self.pushButton_2.clicked.connect(self.orFunc)
        #not
        self.pushButton_3.clicked.connect(self.notFunc)
        #计算
        self.pushButton_4.clicked.connect(self.zuoFunc)
        self.pushButton_5.clicked.connect(self.youFunc)
        self.pushButton_6.clicked.connect(self.cal)

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

    def zuoFunc(self):
            tp = self.lineEdit.text() + " ( "
            self.lineEdit.setText(tp)
            self.lineEdit.setFocus()

    def youFunc(self):
            tp = self.lineEdit.text() + " ) "
            self.lineEdit.setText(tp)
            self.lineEdit.setFocus()
    def cal(self):
        if self.lineEdit.text():
            # 建立列表
          try:
            my_list = []
            for line in content:
                my_list.append(line.strip())

            # 交集操作函数
            def And(list1, list2):
                return list(set(list1) & set(list2))
            # 并集操作函数
            def Or(list1, list2):
                return list(set(list1) | set(list2))
            # 差集操作函数
            def AndNot(list1, list2):
                return list(set(list1) - set(list2))
            def orNot(list1, list2):
                return list(set(list1) | (set(str(x) for x in range(8000)) - set(list2)))
            def my_not(lis):
                return list(set(str(x) for x in range(8000)) - set(lis))
            def evaluate_expression(expression):
                if len(expression) == 1:
                    return expression[0]
                else:
                    i = 0
                    while i < len(expression):
                        if expression[i] == '(':
                            # 寻找与当前左括号对应的右括号
                            count = 1
                            j = i + 1
                            while j < len(expression):
                                if expression[j] == '(':
                                    count += 1
                                elif expression[j] == ')':
                                    count -= 1
                                    if count == 0:
                                        break
                                j += 1
                            # 递归处理括号内的表达式，并将结果替换为括号的计算结果
                            sub_expression = expression[i + 1:j]
                            sub_result = evaluate_expression(sub_expression)
                            expression[i:j + 1] = [sub_result]
                        i += 1
                    # 处理剩余的表达式，类似之前的代码
                    i = 0
                    if expression[0] != 'not':
                        result = expression[0]
                        i += 1
                    else:
                        i += 2
                        result = my_not(expression[1])
                    while i < len(expression):
                        if expression[i] == 'and':
                            if i < len(expression) - 2 and expression[i + 1] == 'not':
                                word2 = expression[i + 2]
                                word1 = result
                                ll = AndNot(word1, word2)
                                result = ll
                                i += 3
                            elif i < len(expression) - 1:
                                word2 = expression[i + 1]
                                word1 = result
                                ll = And(word1, word2)
                                result = ll
                                i += 2
                        elif expression[i] == 'or':
                            if i < len(expression) - 2 and expression[i + 1] == 'not':
                                word2 = expression[i + 2]
                                word1 = result
                                ll = orNot(word1, word2)
                                result = ll
                                i += 3
                            elif i < len(expression) - 1:
                                word2 = expression[i + 1]
                                word1 = result
                                ll = Or(word1, word2)
                                result = ll
                                i += 2
                        i += 1
                    return result
            # 输入查询词语和选项
            query = self.lineEdit.text()
            query = query.split()
            qqq = []
            for word in query:
                if word == 'and' or word == 'or' or word == 'not' or word == '('or word == ')':
                    qqq.append(word)
                else:
                    query_words = jieba.lcut(word)
                    if len(query_words) == 1:
                        qqq.append(list(inverted_index[word][1].keys()))
            query = qqq
            result = evaluate_expression(query)

            self.textEdit.clear()
            # 打印结果列表中的文档内容
            for doc_id in result:
                self.textEdit.append(my_list[int(doc_id)])
            le ='共有'+str(len(result))+"个相关网站"
            highlighted_text = '<span style="background-color: yellow;">' + le + '</span>'
            self.textEdit.append(highlighted_text)
          except Exception as e:
              QMessageBox.warning(self, "警告", "语法错误", QMessageBox.Yes)
        else:
            QMessageBox.warning(self,"警告","空值",QMessageBox.Yes)

if __name__ == "__main__":
    with open("daopaisuoyin.txt", 'r', encoding='utf-8') as file:
        content = file.read()
    inverted_index = eval(content)
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