from flask import *

import pyrebase
app = Flask(__name__,template_folder='template' )
firebaseConfig = {
  'apiKey': "AIzaSyDlZzw8CXHIiaLXEbq9o6F3cr7JbGNYoKo",
  'authDomain': "disha-61129.firebaseapp.com",
  'databaseURL': "https://disha-61129-default-rtdb.firebaseio.com",
  'projectId': "disha-61129",
  'storageBucket': "disha-61129.appspot.com",
  'messagingSenderId': "489204231107",
  'appId': "1:489204231107:web:76ddb08dc672ec35902b76",
  'measurementId': "G-S6P3Y35CQJ",
  'serviceAccount': "key.json"
}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()
auth= firebase.auth()
storage=firebase.storage()

userDict={}

@app.route('/', methods=['POST', 'GET'])
def landing():
  return 'HELLO'

@app.route('/qr_code', methods=['POST', 'GET'])
def index():
    userName = request.form['sample']

    userDetails= db.child('ProfileData').order_by_child('userName').equal_to(userName).get()
    for i in userDetails.each():
        for key,value in zip(i.val().keys(),i.val().values()):
          userDict[key]=value
            
    return render_template('qr_info.html', userDict = userDict)


if __name__ == 'main':
    app.secret_key= 'super secret key'
    app.run()