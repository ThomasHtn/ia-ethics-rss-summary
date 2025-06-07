from flask import Flask, render_template
import feedparser
from transformers import pipeline

# Config
RSS_FEED_URL = "https://www.google.com/alerts/feeds/01533024866642448805/459010232931657264"
keywords = [
    "éthique de l'intelligence artificielle",
    "éthique de l'IA",
    "IA responsable",
    "biais algorithmiques",
    "transparence des algorithmes",
    "régulation de l'IA",
    "gouvernance de l'intelligence artificielle",
    "dérives de l'intelligence artificielle",
    "justice algorithmique",
    "surveillance algorithmique",
    "discrimination algorithmique",
    "IA et vie privée",
    "encadrement de l'IA",
    "droits humains et intelligence artificielle",
    "AI ethics",
    "ethical AI",
    "responsible AI",
    "algorithmic bias",
    "AI transparency",
    "AI governance",
    "AI accountability",
    "regulation of AI",
    "AI and human rights",
    "ethical implications of AI",
    "ethical machine learning",
    "AI fairness",
    "risks of AI",
    "ethics in artificial intelligence"
]

MAX_ARTICLES = 20

app = Flask(__name__)
summarizer = pipeline("summarization")

def get_filtered_articles():
    feed = feedparser.parse(RSS_FEED_URL)
    articles = []

    for entry in feed.entries:
        if any(kw.lower() in entry.title.lower() or kw.lower() in entry.summary.lower() for kw in KEYWORDS):
            try:
                summary = summarizer(entry.summary, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
            except Exception:
                summary = entry.summary[:300] + '...'
            articles.append({
                'title': entry.title,
                'link': entry.link,
                'summary': summary
            })
        if len(articles) >= MAX_ARTICLES:
            break

    return articles

@app.route('/')
def index():
    articles = get_filtered_articles()
    return render_template('articles.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)