from flask import Flask
from flask import render_template
import datetime
app = Flask(__name__)


@app.route("/")
def hello_world():
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    mydate = datetime.datetime.now()
    mon_year = mydate.strftime("%b %Y")
    date = datetime.date.today().day
    s_date = str(date)
    if int(s_date[-1]) == 1:
        sup = "st"
    elif int(s_date[-1]) == 2:
        sup = "nd"
    elif int(s_date[-1]) == 3:
        sup = "rd"
    else:
        sup = "th"
    now = datetime.datetime.now()
    dt = datetime.datetime.now().weekday()
    day = days[dt]

    current_time = now.strftime("%H:%M:%S")
    time = current_time
    return render_template("index.html",date_html = date,sup_html = sup,mon_year_html = mon_year,day_html=day,time_html=time)

app.run(debug=True)