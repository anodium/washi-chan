#!/usr/bin/env python

import web

web.config.debug = False

urls = (
    '/', 'index',
    '/list', 'postlist',
    '/post', 'newpost'
)

posts = [['Anon', 'Manuel', '0', 'Hey there! Welcome to Washi-chan! To start, just type your reply! (For help, see <a href="/static/help.html">this</a>.)']]

class index:
    def GET(self):
        return "<!doctype html><html><head><title>Washi-chan</title></head><body><iframe width='100%' height='500px' src='/list'></iframe><iframe width='25%' height='150px' src='/post'></iframe></body></html>"
    
    def POST(self):
        postdata = web.input()
        posts.append([str(postdata.name), str(postdata.trip), str(len(posts)), str(postdata.body)])
        return "<html><head><meta http-equiv='refresh' content='2; url=/post'/></head></html>"

class postlist:
    def GET(self):
        hypertext = "<head><meta http-equiv='refresh' content='2'><meta http-equiv='cache-control' content='max-age=0'/><meta http-equiv='cache-control' content='no-cache'/><meta http-equiv='expires' content='0'/><meta http-equiv='expires' content='Tue, 01 Jan 1980 1:00:00 GMT'/><meta http-equiv='pragma' content='no-cache'/><title>Washi-chan</title><link rel='stylesheet' type='text/css' href='/static/styles.css'/></head><body><h1>Washi-chan</h1>"
        for i in posts:
            hypertext += "<hr/><span class='name'>" + i[0] + "</span> (<span class='trip'>" + str(hash(i[1])).encode('base64', 'strict') + "</span>) [<span class='pid'>" + i[2] + "</span>]<br/><div class='mesg'>" + i[3] + "</div>"
        hypertext += "</body></html>"
        return hypertext

class newpost:
    def GET(self):
        return "<form method='post' action='/'><p><input type='text' name='name' value='Name'/><input type='text' name='trip' value='Tripcode'/><textarea rows='2' cols='32' name='body' value='Message'>Message</textarea><input type='submit' name='Post' value='Post'/></p></form>"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
