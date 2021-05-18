#!/usr/bin/python

import flask,time,os,models
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
app=flask.Flask(__name__)
app.secret_key=b'[gsk37837/eshjn\x09\x09ao""\x01\xff\xab\xdd ;a'
cors=CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/auth/',methods=['GET','POST'])
def auth():
    if flask.request.method=='POST':
        form= flask.request.form
        meno=form['ucitelka']
        if meno == '123321':
            flask.session['allwd']=True
            return flask.redirect('/ukaz/')
        else:
            return flask.render_template('index.html',error='Asi si zadal zly kod!')
            
    return flask.abort(401)

@app.route('/ukaz/',methods=['GET','POST'])
def ukaz():

    if not flask.session.get('allwd',False):
        return flask.redirect('/')
    if flask.request.method=='POST':
        flask.session['user']=flask.request.form['nick']
        return flask.redirect('/forum/')
    
    return flask.render_template('ukaz.html')

@app.route('/forum/' , methods=['GET','POST'])
def forum():
    if 'user' not in flask.session:
        return flask.redirect('/')
    curuser=flask.session['user']
    return flask.render_template('forum.html',usrname=curuser)

@app.route('/forum/table/')
@cross_origin()
def table():
    if 'user' not in flask.session:
        return flask.redirect('/')
  
    curuser=flask.session['user']
    prispevky=models.all_p() 
    return flask.render_template('table.html',prispevky=prispevky)

@app.route('/forum/add/',methods=['POST','GET'])
def pridaj():
    if flask.request.method=='POST':
        if 'user' not in flask.session:
            return flask.redirect('/')

        curuser=flask.session['user']
        form=flask.request.form
        text=form['prispevok']
        timem=time.ctime(time.time())
        author=curuser
        models.Prispevok(author,timem,text)
        return flask.redirect('/forum/')
    return flask.redirect('/')

@app.route('/logout/')
def odhlas():
    del flask.session['user']
    return flask.redirect('/ukaz/')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return flask.send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
if __name__=='__main__':
      
    app.run(debug=True)
