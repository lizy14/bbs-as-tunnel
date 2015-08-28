import urllib
import urllib.request
import urllib.parse
from LearnPageParser import LearnPageParser

class LearnTransferHandler:
	baseURL = '://learn.tsinghua.edu.cn/MultiLanguage/'
	
	def login(self):
		loginURL = 'https'+self.baseURL+'lesson/teacher/loginteacher.jsp'
		loginPostData = urllib.parse.urlencode({
			'leixin1'  :'student',
			'userid'   :self.userid,
			'userpass' :self.userpass
		})
		self.opener.open(loginURL,loginPostData.encode())
		
	def __init__(self, userid, userpass, bbs_id, course_id, talk_id):
		self.userid = userid
		self.userpass = userpass
		self.bbs_id = bbs_id
		self.course_id = course_id
		self.talk_id = talk_id
		self.opener = urllib.request.build_opener(
			urllib.request.HTTPCookieProcessor())
		self.login()
		
	def get(self):
		getURL = 'http'+self.baseURL+'public/bbs/talk_reply_student.jsp'
		getURL = getURL + '?' + urllib.parse.urlencode({
			'bbs_id'   :self.bbs_id,
			'course_id':self.course_id,
			'id'       :self.talk_id,
			'rep_num'  :'1',
			'up_url'   :'talk_list_student.jsp',
			'default_cate_id':'1'
		})
		return LearnPageParser.do(self.opener.open(getURL).read().decode())
		
	def post(self,data):
		postURL = 'http'+self.baseURL+'public/bbs/bbs_talk_reply_submit.jsp'
		postPostData = urllib.parse.urlencode({
			'saveDir'       :self.course_id+'/bbsfile/',
			'post_bbs_id'   :self.bbs_id,
			'course_id'     :self.course_id,
			'post_par_id'   :self.talk_id,
			'post_up_url'   :'talk_reply_student.jsp',
			'post_file_link':'',
			'filename'      :'',
			'css_name'      :'',
			'tmpl_name'     :'',
			'url_post'      :'/MultiLanguage/public/bbs/bbs_talk_reply_submit.jsp',
			'errorURL'      :'/uperror.jsp?error=',
			'post_cate_id'  :'1',
			'post_title'    :'',#
			'post_detail'   :data,
			'Submit'        :'提交'
		})
		self.opener.open(postURL, postPostData.encode())
		
	def delete(self,id):
		deleteURL = 'http'+self.baseURL+'public/bbs/talk_manager_action.jsp'
		deleteURL = deleteURL + '?' + urllib.parse.urlencode({
			'bbs_id'   :self.bbs_id,
			'userType' :'S',
			'course_id':self.course_id,
			'par_id'   :self.talk_id,
			'note_id'  :id,
			'Submit'   :'del',
			'default_cate_id':'1'
		})
		self.opener.open(deleteURL)
