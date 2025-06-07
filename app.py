from flask import Flask, render_template
import feedparser
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# Config
RSS_FEED_URL = "https://www.google.com/alerts/feeds/01533024866642448805/459010232931657264"
KEYWORDS = [
    "éthique de l'intelligence artificielle",
    "éthique de l'IA",
    "IA responsable",
    "régulation de l'IA",
    "IA et vie privée",
    "encadrement de l'IA",
    "droits humains et intelligence artificielle",
    "AI ethics",
    "ethical AI",
    "responsible AI",
    "regulation of AI",
    "AI and human rights",
    "ethical implications of AI",
    "ethical machine learning",
    "AI fairness",
    "risks of AI",
    "ethics in artificial intelligence"
]

MAX_ARTICLES = 50
MAX_TEXT_LENGTH = 512  # max tokens to avoid memory error

app = Flask(__name__)

# Résumeur (en français)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", tokenizer="facebook/bart-large-cnn", device=-1)

# Traducteur NLLB - version allégée
translator_model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
translator_tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")

def translate_to_french(text):
    inputs = translator_tokenizer(
        text[:MAX_TEXT_LENGTH], return_tensors="pt", truncation=True, max_length=MAX_TEXT_LENGTH
    )
    outputs = translator_model.generate(
        **inputs,
        forced_bos_token_id=translator_tokenizer.lang_code_to_id["fra_Latn"],
        max_length=MAX_TEXT_LENGTH
    )
    return translator_tokenizer.decode(outputs[0], skip_special_tokens=True)

def get_filtered_articles():
    feed = feedparser.parse(RSS_FEED_URL)
    articles = []

    for entry in feed.entries:
        if any(kw.lower() in entry.title.lower() or kw.lower() in entry.summary.lower() for kw in KEYWORDS):
            try:
                # Traduire vers FR
                translated = translate_to_french(entry.summary)
                # Résumer
                summary = summarizer(translated, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
            except Exception as e:
                print(f"[Erreur] {e}")
                summary = f"[Erreur de résumé] {entry.summary[:300]}..."
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