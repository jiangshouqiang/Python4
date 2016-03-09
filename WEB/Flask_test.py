from flask import Flask,render_template
from flask import request

app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')
    # return '<h1>Home</h1>'

@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('from.html',message='this is the world')
@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello,admin</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()