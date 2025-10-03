
'''
news_app/
│── app.py
│── news_api.py
│── templates/
│    └── index.html

'''
from flask import Flask, render_template, request
from news_api import NewsAPI

app = Flask(__name__)

# Replace with your NewsAPI key
API_KEY = "ee2bf3c2df0d4ae1a917a6ad82efd25a"
news_api = NewsAPI(API_KEY)

@app.route("/", methods=["GET", "POST"])
def index():
    category = None
    headlines = []

    if request.method == "POST":
        category = request.form.get("category")
        headlines = news_api.get_headlines(category=category)
        print("Number of articles fetched:", len(headlines))

    return render_template("index.html", headlines=headlines, category=category)

if __name__ == "__main__":
    app.run(debug=True)
