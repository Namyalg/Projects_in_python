from flask import Flask, render_template
from pymongo import MongoClient
client = MongoClient('mongodb+srv://remo:remo@cluster0.ireie.mongodb.net/add_user?retryWrites=true&w=majority')

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")
    return("hello")

if __name__ == "__main__":
    print(client.sample_airbnb.listingsAndReviews.find_one({"name" : "Namya LG"}))
    app.run(port=8000)
