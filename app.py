from flask import Flask, render_template, request
from knowledge_databases import add_article, query_all_articles


app = Flask(__name__)


@app.route('/')
def root():
    return render_template("index.html", articles=query_all_articles())

@app.route('/articles', methods=["POST"])
def post_articles():
    name = request.form['name']
    topic = request.form['topic']
    rating = request.form['rating']
    add_article(name, topic, rating)
    return render_template("index.html", created=True, articles=query_all_articles())

if __name__ == '__main__':
    app.run(debug=True)
