import mysql.connector
import json
import threading


class Database:
	def __init__(self):
# 		print 'init data'
		self.cn = mysql.connector.connect(user='root', password='Rvpooh123', database='sdc')

	def insert(self, data):
		sql = """insert into feature_model 
		(user_id, post_id, poster_name, rating, is_location, share, comment, like_number, vdo, image, url, create_date)
		values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, now())"""
		user_id = data['user_id']
		post_id = data['post_id']
		poster_name = data['poster_name']
		rating = data['rating']
		is_location = data['is_location']
		share = data['share']
		comment = data['comment']
		like = data['like_number']
		vdo = data['vdo']
		image = data['image']
		url = data['url']
		try:
			self.cursor = self.cn.cursor()
			self.cursor.execute(sql,(user_id, post_id, poster_name, rating, is_location, share, comment, like, vdo, image, url))
			self.cn.commit()
			self.cursor.close()			
		except Exception, e:
			print e

	def insert2(self, data):
		sql = """insert into feature_model 
		(user_id, post_id, poster_name, rating, is_location, share, comment, like_number, vdo, image, url, tags_number, create_date)
		values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, now())"""
		user_id = ''
		post_id = ''
		poster_name = data['user_name']
		rating = data['rating']
		is_location = data['is_location']
		share = data['share']
		comment = data['comment']
		like = data['like_number']
		vdo = data['vdo']
		image = data['image']
		url = data['url']
		hashtag = data['hashtag']
		try:
			self.cursor = self.cn.cursor()
			self.cursor.execute(sql,(user_id, post_id, poster_name, rating, is_location, share, comment, like, vdo, image, url, hashtag))
			self.cn.commit()
			self.cursor.close()			
		except Exception, e:
			print e
	
	def insert_filter_el(self, data):
		sql = """insert into filter_el 
		(message, sholdbe, create_date)
		values (%s, %s, now())"""
		sholdbe = data['sholdbe']
		message = data['message']
		
		try:
			self.cursor = self.cn.cursor()
			self.cursor.execute(sql,(message, sholdbe))
			self.cn.commit()
			self.cursor.close()			
		except Exception, e:
			print e	

	def insert_filter_el_2(self, data):
		sql = """insert into filter_el 
		(message, sholdbe, user_post, create_date)
		values (%s, %s, %s, now())"""
		sholdbe = data['sholdbe']
		message = data['message']
		user_post = data['user_post']
		
		try:
			self.cursor = self.cn.cursor()
			self.cursor.execute(sql,(message, sholdbe, user_post))
# 			print sql
			self.cn.commit()
			self.cursor.close()			
		except Exception, e:
			print e
				
	def insert_feedback(self, data):
		sql = """insert into feed_back 
		(feed_back, rating, is_location, share, comment, 
		like_number, vdo, image, url, tags_number, 
		user_post, user_feed_back, message, create_date)
		values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, now())"""
		
		feed_back = data['feed_back']
		rating = data['rating']
		is_location = data['is_location']
		share = data['share']
		comment = data['comment']
		like = data['like_number']
		vdo = data['vdo']
		image = data['image']
		url = data['url']
		hashtag = data['hashtag']
		user_post = data['user_post']
		user_feed_back = data['user_feed_back']
		message = data['message']
		try:
			self.cursor = self.cn.cursor()
			self.cursor.execute(sql,(feed_back, rating, is_location, share, comment, like, vdo, image, url, hashtag, user_post, user_feed_back, message))
			self.cn.commit()
			self.cursor.close()			
		except Exception, e:
			print e
	
	def select_filter_el(self):
		sql = 'select message from filter where sholdbe = "no"'
		ret = []
		try:
			self.cursor = self.cn.cursor()
			self.cursor.execute(sql)
# 			print sql
			for (message) in self.cursor:
# 				print 'msg ',message[0]
				ret.append(message[0])
		except Exception, e:
			print e
		return ret
	
	def insert_fb_filter_save(self, data):
		sql = """insert into fb_filter_assessment 
		(meesage, user_post, filter_status, agree_value, create_date) values (%s, %s, %s, %s, now())""";
		message = data['message']
		user_post = data['user_post']
		agree_value = data['agree_value']
		filter_status = data['filter_status']
		
		try:
			self.cursor = self.cn.cursor()
			self.cursor.execute(sql,(message, user_post, filter_status, agree_value))
			print sql
			self.cn.commit()
			self.cursor.close()			
		except Exception, e:
			print e		
	
	def select_inv_fbfiler(self, sql):
		ret = []
		try:
			self.cursor = self.cn.cursor()
			self.cursor.execute(sql)
			for (message) in self.cursor:
				ret.append(message[0])
		except Exception, e:
			print e
		self.cursor.close()
		return ret
	
	def insert_training_data(self, dict):
		self.template_persist(dict, 'training_data')
	
	def template_persist(self, dict, table_name):
		sql_file = ""
		sql_value = ""
		t_value = []
		for k, v in dict.items():
			sql_file += k+","
			sql_value += "%s,"
			t_value.append(v)
		sql_file = sql_file[:-1]
		sql_value = sql_value[:-1]
		sql = "insert into "+table_name+"("+sql_file+") values ("+sql_value+")"
		try:
			self.cursor = self.cn.cursor()
			self.cursor.execute(sql, t_value)
# 			print sql
			self.cn.commit()
			self.cursor.close()			
		except Exception, e:
			print e		
	
	def select_q(self, sql):
		ret = []
		try:
			self.cursor = self.cn.cursor()
			self.cursor.execute(sql)
			for t in self.cursor:
				ret.append(t)
		except Exception, e:
			print e
		self.cursor.close()
		return ret
	
	def commit(self):
		self.cn.commit()

	def close(self):
		self.cursor.close()
		self.cn.close()

	def close_connection(self):
		self.cn.close()

