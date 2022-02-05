from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "needmorecoffee"

@app.route('/')
def index():
    if 'random' and 'tries' not in session:
        session['random']= random.randint(1,100)
        session['tries'] = 0
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['guess']) == 0:
        session['warning'] = f"<p>you must enter a number!</p>"
        return redirect('/')
    else:
        session['user_guess'] = int(request.form['guess'])
        print(f"user guessed {session['user_guess']}")
        session['tries'] += 1
        if 'warning' in session: 
            session.pop('warning')
            return redirect("/")
        return redirect("/")


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)