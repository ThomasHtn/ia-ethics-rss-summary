from flask import Flask, render_template, send_file
import feedparser
import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from langdetect import detect
from bs4 import BeautifulSoup
import os

# --- Config ---
RSS_FEED_URL = "https://www.google.com/alerts/feeds/01533024866642448805/459010232931657264"
KEYWORDS = [
    "éthique de l'intelligence artificielle", "éthique de l'IA", "IA responsable",
    "régulation de l'IA", "IA et vie privée", "encadrement de l'IA",
    "droits humains et intelligence artificielle", "AI ethics", "ethical AI",
    "responsible AI", "regulation of AI", "AI and human rights",
    "ethical implications of AI", "ethical machine learning", "AI fairness",
    "risks of AI", "ethics in artificial intelligence"
]
MAX_ARTICLES = 50
MAX_TEXT_LENGTH = 512

app = Flask(__name__)

# --- Models setup ---
DEVICE = 0 if torch.cuda.is_available() else -1

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    tokenizer="facebook/bart-large-cnn",
    device=DEVICE
)

model_name = "facebook/nllb-200-distilled-600M"
translator_model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
translator_tokenizer = AutoTokenizer.from_pretrained(model_name)
french_lang_token_id = translator_tokenizer.convert_tokens_to_ids("<2fra_Latn>")

# --- Helper functions ---

def clean_text(html_text):
    """Strip HTML and truncate text."""
    text = BeautifulSoup(html_text, "html.parser").get_text()
    return text.replace('\n', ' ').replace('\r', '').strip()[:MAX_TEXT_LENGTH]

def translate_to_french(text):
    """Detect language and translate to French if needed."""
    try:
        lang = detect(text)
    except:
        lang = "unknown"
    if lang == "fr":
        return text
    try:
        inputs = translator_tokenizer(text[:MAX_TEXT_LENGTH], return_tensors="pt", truncation=True, max_length=MAX_TEXT_LENGTH)
        outputs = translator_model.generate(**inputs, forced_bos_token_id=french_lang_token_id, max_length=MAX_TEXT_LENGTH)
        return translator_tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        print(f"[Translation Error] {e}")
        return text

def summarize(text):
    """Clean, translate if needed, then summarize text."""
    cleaned = clean_text(text)
    try:
        translated = translate_to_french(cleaned)
        summary = summarizer(translated, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
        return summary
    except Exception as e:
        print(f"[Summarization Error] {e}")
        return f"[Summary Error] {cleaned[:300]}..."

def fetch_articles():
    """Fetch RSS, filter by keywords, summarize, and return articles list."""
    feed = feedparser.parse(RSS_FEED_URL)
    articles = []

    for entry in feed.entries:
        title = clean_text(entry.title)
        summary = clean_text(entry.summary)
        combined = f"{title} {summary}".lower()
        if any(kw.lower() in combined for kw in KEYWORDS):
            articles.append({
                'title': title,
                'link': entry.link,
                'summary': summarize(summary)
            })
            if len(articles) >= MAX_ARTICLES:
                break
    return articles

def save_as_markdown(articles, filename="articles_summary.md"):
    """Save articles list as a markdown file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# AI Ethics Articles Summary\n\n")
        for art in articles:
            f.write(f"## [{art['title']}]({art['link']})\n\n{art['summary']}\n\n---\n\n")

# --- Flask routes ---

@app.route('/')
def index():
    articles = fetch_articles()
    return render_template('articles.html', articles=articles)

@app.route('/download_markdown')
def download_markdown():
    articles = fetch_articles()
    save_as_markdown(articles)
    path = "articles_summary.md"
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    return "Markdown file not found.", 404

# --- Run app ---
if __name__ == '__main__':
    app.run(debug=True)