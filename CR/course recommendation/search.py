#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.decorators import csrf
from sklearn import metrics
from sklearn.cluster import KMeans 
from sklearn import metrics
from math import sqrt
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.metrics import mean_squared_error
from math import sqrt
import pymysql
import os
import numpy as np
import matplotlib as plt

# 表单
def search_form(request):
    return render_to_response('search_form.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = 'you get: ' + request.GET['q']
    else:
        message = 'you none'
    return HttpResponse(message)

def getkc(request):  ## 获取全部课程
	conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='ccnuss', charset='utf8')
	cursor = conn.cursor()
	sql = "SELECT * FROM ccnuss ORDER BY  RAND() limit 100 " 
	cursor.execute(sql)   
	json = "{" 
	json += "\"total\":20,"   
	json += "\"rows\":["   
	results = cursor.fetchall()
	for rs in results:
	    json += "{\"cell\":[\""+str(rs[0])+"\",\""+str(rs[1])+"\",\""+str(rs[2])+"\",\""+str(rs[3])+"\",\""+str(rs[4])+"\",\""+str(rs[5])+"\",\""+str(rs[8])+"\",\""+str(rs[7])+"\",\""+str(rs[6])+"\"]}"
	    json += ","
	json += "{\"cell\":[\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\"]}"
	json += "]}" 
	f = open('./static/data/test.json', 'w',encoding='utf8')
	f.write(json)
	f.close()
	#return HttpResponse("It Worked")
	return render_to_response('webSet.html')
	pass

def recommend(request):
	ctx ={}
	conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='ccnuss', charset='utf8')
	cursor = conn.cursor()
	if request.POST:
		ctx['rlt'] = request.POST['q']
	if not ctx.get('rlt'):
		json = "{"
		json += "\"total\":2,"   
		json += "\"rows\":["   
		json += "{\"cell\":[\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\"]}"
		json += "]}" 
		f = open('./static/data/xsxk.json','w',encoding='utf8')
		f1 = open('./static/data/JSONData.json','w',encoding='utf8')
		f.write(json)
		f.close()	
		f1.write(json)
		f1.close()
	else:
		useid = str(ctx.get('rlt'))
		sql = "SELECT * FROM ccnuss where XH_SORT="+useid+" " 
		cursor.execute(sql)   
		json = "{"
		json += "\"total\":1,"   
		json += "\"rows\":["   
		results = cursor.fetchall()
		#results = none
		for rs in results:
		    json += "{\"cell\":[\""+str(rs[0])+"\",\""+str(rs[1])+"\",\""+str(rs[2])+"\",\""+str(rs[3])+"\",\""+str(rs[4])+"\",\""+str(rs[5])+"\",\""+str(rs[8])+"\",\""+str(rs[7])+"\",\""+str(rs[6])+"\",\""+str(rs[10])+"\"]}"
		    json += ","
		json += "{\"cell\":[\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\"]}"
		json += "]}" 
		f = open('./static/data/xsxk.json', 'w',encoding='utf8')
		f.write(json)
		f.close()
		#return HttpResponse("It Worked")
		#推荐部分__________
		##
		sql = "SELECT * FROM ccnuss " 
		cursor.execute(sql)          
		results = cursor.fetchall()     # 获取所有记录列表
		x_list = []
		y_list = []
		for row in results:    
			x_list.append([(row[11]),(row[12])])
			y_list.append(row[10]) 

		X = np.array(x_list)
		y = np.array(y_list,dtype='int')

		X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

		n_users = np.count_nonzero(np.unique(X[:,0]))
		n_items = np.count_nonzero(np.unique(X[:,1]))

		train_access_matrix = np.zeros((n_users, n_items))
		index = 0
		while index<X_train.shape[0]:
			train_access_matrix[X_train[index][0]-1, X_train[index][1]-1] = y_train[index]
			index = index + 1

		test_access_matrix = np.zeros((n_users, n_items))
		index = 0
		while index<X_test.shape[0]:
			test_access_matrix[X_test[index][0]-1, X_test[index][1]-1] = y_test[index]
			index = index + 1
		
		user_similarity = pairwise_distances(train_access_matrix, metric='cosine')    #基于用户
		item_similarity = pairwise_distances(train_access_matrix.T, metric='cosine')  #基于项目

		item_prediction = predict(train_access_matrix, item_similarity, type='item') #基于用户
		user_prediction = predict(train_access_matrix, user_similarity, type='user') #基于项目

		same = 5                         # 两种模型均先推荐课数初始值
		control_index = 5                # 推荐课程门数
		re_array = recommand_lessons(useid,same,item_prediction,user_prediction)
		while len(re_array)!=control_index:          
			same += 1
			re_array = recommand_lessons(useid,same,item_prediction,user_prediction)


		json = "{"
		json += "\"total\":1,"   
		json += "\"rows\":["  
		for i in re_array:
			cursor = conn.cursor()
			sql = "SELECT * FROM ccnuss where KC_SORT="+str(i)+" LIMIT 1" 
			cursor.execute(sql)     
			results = cursor.fetchall()     # 获取所有记录列表
			#results = none
			for rs in results:
			    json += "{\"cell\":[\""+str(rs[2])+"\",\""+str(rs[3])+"\",\""+str(rs[4])+"\",\""+str(rs[5])+"\",\""+str(rs[6])+"\",\"\",\""+str(rs[7])+"\",\""+str(rs[8])+"\"]}"
			    json += ","
		json += "{\"cell\":[\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\"]}"
		json += "]}" 
		f = open('./static/data/JSONData.json', 'w',encoding='utf8')
		f.write(json)
		f.close()


	return render(request,'userInfo.html',ctx)
	pass

#####  功能函数
#
def matrix(useid):
	pass
def test(request):
	return render_to_response('smsInfo.html')
	pass

def rmse(prediction, ground_truth):
    prediction = prediction[ground_truth.nonzero()].flatten()
    ground_truth = ground_truth[ground_truth.nonzero()].flatten()
    return sqrt(mean_squared_error(prediction, ground_truth))

def predict(ratings, similarity, type='user'):
    if type == 'user':
        mean_user_rating = ratings.mean(axis=1)
        #You use np.newaxis so that mean_user_rating has same format as ratings
        ratings_diff = (ratings - mean_user_rating[:, np.newaxis])
        pred = mean_user_rating[:, np.newaxis] + similarity.dot(ratings_diff) / np.array([np.abs(similarity).sum(axis=1)]).T
    elif type == 'item':
        pred = ratings.dot(similarity) / np.array([np.abs(similarity).sum(axis=1)])    
    return pred

def recommand_lessons(user_id,same,item_prediction,user_prediction):     # 推荐函数
    arr1 = np.argsort(user_prediction[int(user_id)-1,:])
    arr2 = np.argsort(item_prediction[int(user_id)-1,:])
    arr1 = arr1[-same:]
    arr2 = arr2[-same:]
    tmp = [val for val in arr1 if val in arr2]
    return tmp

