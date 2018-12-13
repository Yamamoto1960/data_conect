# -*- coding: utf-8 -*-
import json
import codecs
import collections as cl
import sys
import MeCab
import csv

#def json_load_test(path):

def wakati(input_str):
        '''分かち書き用関数
        引数 input_str : 入力テキスト
        返値 m.parse(wakatext) : 分かち済みテキスト'''
        wakatext = input_str
        m = MeCab.Tagger('-Owakati')
        #print(m.parse(wakatext))
        return m.parse(wakatext)


count = 1
#json_file =  codecs.open("split_question_suzukidata/maeda_data0803.json", 'r',encoding="utf-8")
out_csv = open("out_suzukidata_dev_test.csv","w")
#json_file =  codecs.open("split_question_suzukidata_original/test_splitquestion_0801_2_original.json", 'r',encoding="utf-8")
json_file =  codecs.open("/root/data/suzuki_data/split_dev_test/dev.json", 'r',encoding="utf-8")

#json_file =  codecs.open("knowhowQAdata/knowhowQAdata_sent0801.json", 'r',encoding="utf-8")
ys = cl.OrderedDict()
j_data = []
count = 0

for line in json_file:
	writer = csv.writer(out_csv, lineterminator='\n')
	json_dic = json.loads(line)
	#print(json_dic["question"])
	#print(type(json_dic["answer"]))
	#print(json_dic["documents"])
	#print(type(json_dic["documents"]))
	#json_dic2 = dict(json_dic["documents"]
	answer_wakati = wakati(json_dic["answer"]).replace('\n','')
	answer_wakati = answer_wakati.strip()
	#print (answer_wakati)
	#question_wakati = wakati(json_dic["question"]).replace('\n','')
	#question_wakati = question_wakati.strip()
        #print(type(question_wakati))
	###documets部分から、textを抜き出す
	for article in json_dic["documents"]:
		if article["score"] >= 2: 
			#data = cl.OrderedDict()
			#paragraphs_dic =  cl.OrderedDict()
			#paragrahs = []
			#question_dic = cl.OrderedDict()
			#questions = []						
			#answer_dic = cl.OrderedDict()
			#answers = []
			
			paragraph_wakati = wakati(article["text"]).replace('\n','')
			paragraph_wakati = paragraph_wakati.strip()
			#print(paragraph_wakati)
			if paragraph_wakati.find(answer_wakati) == -1:
				continue
			list_C = []
	
			list_C.append(json_dic["question"])
			list_C.append(json_dic["answer"])
			list_C.append(article["text"])
			writer.writerow(list_C)	
			count = count + 1

print(count)			
