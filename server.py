
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
@app.route('/')
def My_page():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)




def write(data):
    with open('database2.csv',newline='', mode='a',) as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']         
        csv_writer = csv.writer(database2, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method =='POST':
      data = request.form.to_dict()
      write(data)
      return redirect("/thanks.html")
    else:
      return "Somthing wrong"  


