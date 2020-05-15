from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/<path>")
def newPath(path):
    return render_template(path)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("./thankyou.html")
        except:
            return "something wrong with the data or paths so can't save to the database"
    else:
        return "something went wrong"

def write_to_file(data):
    with open("database.txt",mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
    with open("database.csv",mode="a",newline="") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter=",",quotechar="\"",quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])