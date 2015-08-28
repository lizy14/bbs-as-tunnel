import re

class LearnPageParser:
	def do(pageHTML):
		
		postsHTML = re.findall('<table id="table_box" cellspacing="1" cellpadding="0">.*?</table>',pageHTML,re.DOTALL)
		posts=[]
		for postHTML in postsHTML:
			try:
				author = re.search('<td width="33%" class="tr2">(.+)?</td>',postHTML).group(1)
				time = re.search('<td width="20%" class="tr2">(.+?)</td>',postHTML,re.DOTALL).group(1).strip()			
				content = re.search('<td colspan="4" class="tr_2" align="left" valign="middle"><p align="left">([^<]*)</p>',postHTML,re.DOTALL).group(1).strip()
			except:
				continue
			post = {
				'author':author,
				'time':time,
				'content':content
			}
			posts.append(post)
		return posts
		