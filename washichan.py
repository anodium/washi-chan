#!/usr/bin/env python

import web
from tripcode import tripcode
import sqlite3

web.config.debug = False

urls = (
	'/', 'index',
	'/list', 'postlist',
	'/post', 'makepost',
	'/help', 'help',
	'/styles.css', 'styles'
)

render = web.template.render('templates')

class index:
	def GET(self):
		return render.frames()

class postlist:
	def GET(self):
		if web.input().b == 'main':
			return render.boardlist()
		db = sqlite3.connect('post.db')
		dbc = db.cursor()
		dbc.execute("SELECT * FROM Post WHERE Board=?", (web.input().b))
		return render.postlist(dbc.fetchall())

class makepost:
	def GET(self):
		return render.makepost()
	
	def POST(self):
		postdata = web.input()
		db = sqlite3.connect('post.db')
		dbc = db.cursor()
		dbc.execute("INSERT INTO Post VALUES (?, ?, ?, ?)", (postdata.board, postdata.name, tripcode(postdata.trip), postdata.body))
		db.commit()
		db.close()
		return render.redirect()

class help:
	def GET(self):
		return render.help()

class styles:
	def GET(self):
		return render.styles()

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
