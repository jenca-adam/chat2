#!/usr/bin/python
import flask,pickle,time,os
from werkzeug.utils import secure_filename
app=flask.Flask(__name__)
povoleny=pickle.load(open('povoleny.pickle','rb'))
prezyvky=pickle.load(open('prezyvky.pickle','rb'))
prispevky=pickle.load(open('prispevky.pickle','rb'))
app.config['UPLOAD_FOLDER']=os.path.join(os.getcwd(),'uploads')
@app.route('/')
def index():
    return flask.render_template('index.html')
@app.route('/auth/',methods=['GET','POST'])
def auth():
    if flask.request.method=='POST':
        form= flask.request.form
        meno=form['ucitelka']
        if meno in['Zingorova','Žingorova','Žingorová','Zingorová']:
            povoleny=pickle.load(open('povoleny.pickle','rb'))
            if flask.request.remote_addr not in povoleny:
                povoleny.append(flask.request.remote_addr)
            with open('povoleny.pickle','wb')as f:
                pickle.dump(povoleny,f)
            return flask.redirect('/ukaz/')
        else:
            return flask.render_template('index.html',error='Asi si zadal zle meno!')
    return flask.abort(401)
@app.route('/ukaz/',methods=['GET','POST'])
def ukaz():
    povoleny=pickle.load(open('povoleny.pickle','rb'))
    if flask.request.remote_addr not in povoleny:
        return flask.redirect('/')
    if flask.request.method=='POST':
        prezyvky[flask.request.remote_addr]=flask.request.form['nick']
        with open('prezyvky.pickle','wb')as f:
                pickle.dump(prezyvky,f)
        return flask.redirect('/forum/')
    
    return flask.render_template('ukaz.html')
@app.route('/forum/' , methods=['GET','POST'])
def forum():
    prezyvky=pickle.load(open('prezyvky.pickle','rb'))
    try:
        curuser=prezyvky[flask.request.remote_addr]
    except KeyError:
        return flask.redirect('/')
            
    return flask.render_template('forum.html',usrname=curuser,prispevky=prispevky)
@app.route('/forum/add/',methods=['POST','GET'])
def pridaj():
    if flask.request.method=='POST':
        curuser=prezyvky[flask.request.remote_addr]

        form=flask.request.form
        text=form['prispevok']
        timem=time.ctime(time.time())
        author=curuser
        prispevky.append([timem,author,text,""])
        pickle.dump(prispevky,open('prispevky.pickle','wb'))
        return flask.redirect('/forum/')
    return flask.redirect('/')
@app.route('/logout/')
def odhlas():
    prezyvky=pickle.load(open('prezyvky.pickle','rb'))
    povoleny=pickle.load(open('povoleny.pickle','rb'))
    povoleny.remove(flask.request.remote_addr)
    del prezyvky[flask.request.remote_addr]
    with open('povoleny.pickle','wb')as f:
                pickle.dump(povoleny,f)
    with open('prezyvky.pickle','wb')as f:
                pickle.dump(prezyvky,f)
    return flask.redirect('/')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return flask.send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
if __name__=='__main__':
      
    app.run(debug=True)
