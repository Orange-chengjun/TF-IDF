import jieba
import jieba.analyse

sentence = "爬虫实验截止时间是这周五，请大家自己申请GitHub账号，或msdn账号，自行上传。同时各位同学将自己的实验打包，包括实验（里面包括代码注释，测试数据集，实验报告等），命名规范是学号+姓名。班长收集整个班级的作业并打包发给我一份，并附上还没有提交的学生名单。"

keywords = jieba.analyse.extract_tags(sentence, topK=20, withWeight=True, allowPOS=('n', 'nr', 'ns'))

for item in keywords:
	print(item[0], item[1])
