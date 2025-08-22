from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Фейковые пользователи (для примера)
users = {
    "test": {"key": "1234", "nickname": "axmetalls", "sub": "02-06-2025", "id": "202"}
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        login = request.form["login"]
        key = request.form["key"]

        if login in users and users[login]["key"] == key:
            return redirect(url_for("profile", user=login))
        else:
            return render_template("login.html", error="❌ Неверный логин или ключ")

    return render_template("login.html")

@app.route("/profile/<user>")
def profile(user):
    data = users.get(user)
    return render_template("profile.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
