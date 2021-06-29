# jobs=SaramInJob+JobKoreaJob

# save_to_file(jobs)
from GetSaramIn import Call_Saramin_Pages
from JobKorea import Get_JobKorea_Pages
from Save import save_to_file
from flask import Flask, render_template, request, redirect, send_file

app = Flask("PowerScrapper")
db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/report")
def report():
    word = request.args.get('word')

    if word:
        word = word.lower()
        fromDB = db.get(word)

        if fromDB:
            JobKoreaJob = fromDB
        else:
            SaramInJob=Call_Saramin_Pages(word)
            JobKoreaJob=Get_JobKorea_Pages(word)
            SaramInJobKoreaJob=SaramInJob+JobKoreaJob

            db[word] = SaramInJobKoreaJob
    else:
        return redirect("/")

    return  render_template("report.html",searchingBy=word, resultNumber=len(SaramInJobKoreaJob),jobs=SaramInJobKoreaJob)


@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")


app.run(host="0.0.0.0", port='5000', debug=True)
