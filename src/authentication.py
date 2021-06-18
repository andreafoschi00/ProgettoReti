''' Progetto di programmazione di reti - Foschi Andrea - Python Web Server '''

from flask import Flask, flash, render_template, request, session
import os

user = "admin"
psw = "admin"

# Creo l'app Flask che sarà necessaria per le operazioni di login/logout
app = Flask(__name__, template_folder="html/")
    
@app.route("/")
def home():
    # Se risulta già loggato si rimanda ad index.html, altrimenti alla pagina di login
    if not session.get("logged_in"):
        return render_template("login.html")
    else:
        return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def do_admin_login():
    # L'operazione di login è una chiamata di tipo POST
    if request.method == "POST":
        userName = request.form["user"]
        password = request.form["psw"]
        account = False
    
    # Controlla che username e password inseriti siano corretti
    if(userName == user and password == psw):
        account = True
    
    if account:
        session["logged_in"] = True
    else:
        flash("Username o password errati.")
    return home()

@app.route("/logout")
def logout():
    session["logged_in"] = False
    return render_template("logout.html")

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=False,host="localhost", port=8080)