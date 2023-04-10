from flask import Flask, render_template, request, jsonify
from VCE import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('interface.html')

@app.route('/process_input', methods=['GET','POST'])
def process_input():
    choice = request.json['choice']
    if EMAIL_ID != "" and PASSWORD != "":
        if choice == 'compose' or choice == 'compose mail':
            message = composeMail()
        elif choice == 'status' or choice == 'mailbox status' or choice == 'stat us':
            message = getMailBoxStatus()
        elif choice == 'search' or choice == 'search mail' or choice == 'mail search':
            message = searchMail()
        elif choice == 'recent' or choice == 'last' or choice == 'last three' or choice == 'sent' or choice == 'last 3':
            message = getLatestMails()
        else:
            message = 'Wrong choice. Please say only the appropriate words'
    else:
        message = 'Both Email ID and Password should be present'

    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=True)
