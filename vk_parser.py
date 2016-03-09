# coding: utf-8
# this is little script for parsing mssages from company page on vk.com (russian social network) and send them to support team in real time

import re
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import urllib2
import profile
import codecs
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#number of last message that we seen
#link = 3400
link = 23

link_current = link 
l = str(link)

addr = 'http://vk.com/beaver_fans?w=wall-96015018_' + l

mess_test = 'test'

title_count=0
title = ''

flag = 0

flag2 = 0
mess = ''

flag1 = 0
mess_name = ''

flag_a = 0
mess_a = ''

#sending messages to zendesk
def fly_to_zendesk (mess, mess_a, addr):

	global t
	# отправитель
	iam = 'adress@example.com'
	to = 'support@companyname.com'
	text1 = 'User '	
	text2 = ' write on your  wall: '
	text3 = ' Please dont answer with Zendesk, answer him here: '

	massiv = [text1, mess_a, text2, mess, text3, addr] 
	text = massiv [0] + massiv [1] + massiv [2] + massiv [3] + massiv [4] + massiv [5]
	
	print text
	
	# header
	subj = 'Тест оповещений вконтакте'
	# SMTP-server for gmail
	server = "smtp.gmail.com"
	port = 25
	#use your own email
	user_name = "adress@example.com"
	user_passwd = "password"
 
	msg = MIMEMultipart('alternative')
	msg['Subject'] = subj
	msg['From'] = iam
	msg['To'] = to

	mime_text = MIMEText(text, 'plain', 'utf-8')
	msg.attach(mime_text)

	# sending
	s = smtplib.SMTP(server, port)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(user_name, user_passwd)
	s.sendmail(iam, to, msg.as_string())
	s.quit()

#parser for title - we need it to check if it is error page
class MyHTMLParser_title(HTMLParser):

	def handle_starttag(self, tag, attrs):
		global title_count
		if tag == 'title':
			title_count=1
		
	def handle_data(self, data):
		global title_count
		global title
		if title_count == 1:
			title = data
			title_count = 0
			
#parser for message			
class MyHTMLParser_text(HTMLParser):

	def handle_starttag(self, tag, attrs):
		if tag == 'div':
			for name, value in attrs:
				if name == 'class' and value == 'pi_text':
					global flag
					flag = 1
						
	def handle_endtag(self, tag):
		if tag != 'div':
			global flag2
			flag2 = 1
        
	def handle_data(self, data):
		global flag
		global flag2
		global mess
		if flag == 1 and flag2 == 1:
			mess = data	
			flag = 0
			flag2 = 0
			

#parser for author of message
class MyHTMLParser_author(HTMLParser):

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for name, value in attrs:
				if name == 'class' and value == 'pi_author':
					global flag_a
					flag_a = 1
							
	def handle_data(self, data):
		global flag_a
		global mess_a
		if flag_a == 1:
			mess_a = data
			flag_a = 0
				
	
parser_title = MyHTMLParser_title()
parser_text = MyHTMLParser_text()
parser_author = MyHTMLParser_author()


while (link >0):
	l = str(link)
	link_current = link
	l_current = str(link_current)
	#we check 50 of messages ahead and looking for messages from users, not error pages and messages from group administrator
	i = 0

	
	while (i <50):
		l = str(link)
		l_current = str(link_current)
		addr = 'http://vk.com/beaver_fans?w=wall-96015018_' + l_current
		contento = urllib2.urlopen(addr).read()
		soup = BeautifulSoup(contento, 'html.parser')
		content_text = str(soup)
		parser_title.feed(contento)
		parser_text.feed(content_text)
		parser_author.feed(contento)

		if title != 'Стена':
			link_current = link_current + 1
			i = i + 1
			print link_current

	
		if title == 'Стена':
			if mess_a != 'Bookmate' and mess_a != 'Восхищенные бобрами':	
				if mess != mess_test:
					fly_to_zendesk (mess, mess_a, addr)
					print '///'
					mess_test = mess
			link = link + 1
			i = 50


	
