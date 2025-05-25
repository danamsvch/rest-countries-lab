from flask import Flask, request

app = Flask(__name__)

@app.route('/myinfo')
def myinfo():
    login = request.args.get('login')
    if login == "is-34fiot-23-168":
        return {
            "login": login,
            "surname": "Мосієвич",
            "name": "Богдана",
            "course": "2",
            "group": "ІС-34"
        }
    else:
        return {"error": "Невірний логін"}, 403

if __name__ == '__main__':
    app.run(debug=True)
