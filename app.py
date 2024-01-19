from flask import Flask, render_template
import os

app = Flask(__name__)

IMG_FOLDER = os.path.join("static", "image")

app.config["UPLOAD_FOLDER"] = IMG_FOLDER

@app.route("/mainpage", methods=["GET"])
def mainpage():
    Flask_Logo = os.path.join(app.config["UPLOAD_FOLDER"], "WebDesignLogo.png")
    Flask_Image = os.path.join(app.config["UPLOAD_FOLDER"], "bookImage_1.jpg")
    return render_template("mainpage.html", user_image=Flask_Logo, topic_image=Flask_Image)

@app.route("/calender", methods=["GET"])
def calender():
    Flask_Logo = os.path.join(app.config["UPLOAD_FOLDER"], "WebDesignLogo.png")
    return render_template("calenderpage.html", user_image=Flask_Logo)

@app.route("/category", methods=["GET"])
def category():
    Flask_Logo = os.path.join(app.config["UPLOAD_FOLDER"], "WebDesignLogo.png")
    return render_template("categorypage.html", user_image=Flask_Logo)

@app.route("/history", methods=["GET"])
def history():
    Flask_Logo = os.path.join(app.config["UPLOAD_FOLDER"], "WebDesignLogo.png")
    return render_template("history.html", user_image=Flask_Logo)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=2010)