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
#input_csv = "labeles_QAC_pair_1203_maeyamamoto.csv" # Data[Question,Answer,Context]
input_csv_knowhouq = "QAC_test1206.csv"
input_csv_suzukiq = "out_suzukidata_test.csv"

ys = cl.OrderedDict()
j_data = []
count_y = 0
count_or = 0
question_or = "kari_question"
count_suzuki = 0

with open(input_csv_knowhouq, 'r') as f:
	reader = csv.reader(f)
	#header = next(reader)  # ヘッダーを読み飛ばしたい時

	for row in reader:
		if count > -1:	#条件付(if)
			#print row[0]          # 1行づつ取得できる

			data = cl.OrderedDict()
			paragraphs_dic =  cl.OrderedDict()
			paragrahs = []
			question_dic = cl.OrderedDict()
			questions = []
			answer_dic = cl.OrderedDict()
			answers = []

			if row[5].find("y") != -1: #やりすぎを排除する場合はここを利用
				#print (row[1])
				#print (row[4])
				#question_wakati = wakati(row[0]).replace('\n','')
				#question_wakati = question_wakati.strip()
				answer_wakati = wakati(row[1]).replace('\n','')
				answer_wakati = answer_wakati.strip()
				#paragraph_wakati = wakati(row[3]).replace('\n','')
				#paragraph_wakati = paragraph_wakati.strip()

				count_y += 1
			
			elif row[5].find("or") != -1:
				#print row[1]
				#print row[4]
				count_or += 1
				#question_or = row[0]
				if row[0] != question_or:
					#print ("main_question:"+"\t"+row[0])
					#print ("main_ans:"+"\t"+row[4])
					question_or = row[0]
					answer_wakati = wakati(row[1]).replace('\n','')
					answer_wakati = answer_wakati.strip()

				else:
					#print ("sub_question:"+"\t"+row[0])
					#print ("sub_ans:"+"\t"+row[4])
					row[6] = "or_sub"
					#print(row[6])
					continue
			
			else:
				answer_wakati = wakati(row[1]).replace('\n','')
				answer_wakati = answer_wakati.strip()
				
	
			question_wakati = wakati(row[0]).replace('\n','')
			question_wakati = question_wakati.strip()
			#answer_wakati = wakati(row[4]).replace('\n','')
			#answer_wakati = answer_wakati.strip()
			paragraph_wakati = wakati(row[3]).replace('\n','')
			paragraph_wakati = paragraph_wakati.strip()			
			#print(paragraph_wakati)
			#print(answer_wakati)
			if (paragraph_wakati.find(answer_wakati) == -1) or (row[6] == "or_sub") or (len(answer_wakati) <= 0):
				print("/////")
				print(answer_wakati)
				print(paragraph_wakati)
				print("/////")
				#print("ok"))
				continue

			#print(paragraph_wakati)
			#print(question_wakati)
			print(answer_wakati)
			#if len(answer_wakati) <= 0:
				#print(count)
				#print(question_wakati)
				#print(answer_wakati)
				#print(paragraph_wakati)
				#print("////")
				#print(row)
				#continue
			#if count == 333:
				#print(question_wakati)
				#print(answer_wakati)
				#print(paragraph_wakati)
			answer_dic = {"answer_start":paragraph_wakati.find(answer_wakati) ,"text":answer_wakati} #答えの直前の開始位置を代入
			#print(paragraph_wakati.find(answer_wakati))
			#print(paragraph_wakati[paragraph_wakati.find(answer_wakati)])
			#print(paragraph_wakati[paragraph_wakati.find(answer_wakati) -1])
			answers = [answer_dic]
			question_dic = {"answers":answers,"question":question_wakati,"id":count}
			questions = [question_dic]
			paragraphs_dic = {"context":paragraph_wakati,"qas":questions}
			paragraphs = [paragraphs_dic]
			#data["title"] = article["text"]
			data = {"title":"test_title", "paragraphs":paragraphs}
			j_data.append(data)
			#paragraph["context"] = article["text"]
			#print(article["title"])
			count = count + 1 # id
			#print(article["score"])
			#print(article["text"])
			#print("///////////////")
			#print(json_dic2["title"])
			#ys["data"].extend(data)
	#print("\n\n")

#以下鈴木データ処理
print(count)

with open(input_csv_suzukiq, 'r') as f2:
	reader2 = csv.reader(f2)

	for row in reader2:
		if count > -1: #条件付(if)
			#print row[0]          # 1行づつ取得できる
			data = cl.OrderedDict()
			paragraphs_dic =  cl.OrderedDict()
			paragrahs = []
			question_dic = cl.OrderedDict()
			questions = []
			answer_dic = cl.OrderedDict()
			answers = []

			question_wakati = wakati(row[0]).replace('\n','')
			question_wakati = question_wakati.strip()
			answer_wakati = wakati(row[1]).replace('\n','')
			answer_wakati = answer_wakati.strip()
			paragraph_wakati = wakati(row[2]).replace('\n','')
			paragraph_wakati = paragraph_wakati.strip()
			if paragraph_wakati.find(answer_wakati) == -1:
				print(answer_wakati)
				#print(paragraph_wakati)
				print("ok")
				continue
			
			#if count == 107:
				#print(row[2])
				#print(row[0])

			answer_dic = {"answer_start":paragraph_wakati.find(answer_wakati) ,"text":answer_wakati} #答えの直前の開始位置を代入
			#print(paragraph_wakati.find(answer_wakati))
			#print(paragraph_wakati[paragraph_wakati.find(answer_wakati)])
			#print(paragraph_wakati[paragraph_wakati.find(answer_wakati) -1])
			answers = [answer_dic]
			question_dic = {"answers":answers,"question":question_wakati,"id":count}
			questions = [question_dic]
			paragraphs_dic = {"context":paragraph_wakati,"qas":questions}
			paragraphs = [paragraphs_dic]
			#data["title"] = article["text"]
			data = {"title":"test_title", "paragraphs":paragraphs}
			j_data.append(data)
			#paragraph["context"] = article["text"]
			#print(article["title"])
			count = count + 1 # id
			count_suzuki = count_suzuki + 1


ys["data"] = j_data
ys["version"] = 1.1
json.dump(ys ,open('./question_normal/test_connect-v1.1.json','w',encoding="utf-8"),ensure_ascii=False)
#json.dump(ys ,open('test-v1.1.json','w'),ensure_ascii=False)
print(count)
print(count_suzuki)
#print (count_y)
#print(count_or)
