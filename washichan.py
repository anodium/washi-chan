#!/usr/bin/env python

import web
from tripcode import tripcode
import sqlite3

web.config.debug = False

urls = (
	'/', 'index'
)

render = web.template.render('templates')

class index:
	def GET(self):
		db = sqlite3.connect('board.db')
		dbc = db.cursor()
		dbc.execute('select * from posts')
		posts = dbc.fetchall()
		db.close()
		return render.index(posts)
	
	def POST(self):
		db = sqlite3.connect('board.db')
		dbc = db.cursor()
		dbc.execute('insert into posts values (?, ?, ?)', (web.input().name, tripcode(web.input().trip), web.input().mesg))
		db.commit()
		dbc.execute('select * from posts')
		posts = dbc.fetchall()
		db.close()
		return render.index(posts)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
