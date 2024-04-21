共有三个功能 分别是：
（1）多运算符的混合布尔查询 
（2）多运算符的短语混合布尔查询
（3）ltc.ltc方法对and查询或or查询（可含not）排序

其中，功能（1）运行boolmixpro.py即可
功能（2）运行locationmixplus.py即可
功能（3）运行vectorspace.py即可

其他没有直接用到的py文件中：
drawl.py用于爬取网页信息，preprocess.py用于对爬取的信息做预处理,create.py用于整合文本docID到文本中的词语的映射，便于在后面的排序操作获得符合要求的文本中出现的所有词项从而构建向量矩阵时使用。
daopaisuoyinbiao.py用于构建倒排索引表，daopaisuoyindaiweizhi.py用于构建带有位置信息的倒排索引表。
Untitledpro.py用于设置功能（1）的界面，untitledlocationplus.py用于设置功能（2）的界面，untitledVSModel.py用于设置功能（3）的界面

其中，在利用向量空间模型进行排序时，以纯and操作为例，为了节省时间，先算出来包含所有输入的查询词语的docID,再获得这些docID对应的文本文件里出现的所有词项。为了获得符合要求的docID对应的文本里出现的所有词语，专门构建了一个类似的表格，以docID为键，以该docID对应的文本中出现的单词集合组成的列表为值（可以保证不重复）。这个表格命名为dictionary2.txt

tingyongci.txt存放了从网上下载的常见停用词，lianjie.txt存放了与docID对应的链接，用于反馈给用户。
