import re
from collections import Counter

# -----------------------------
# Sample tourism posts (replace with your own dataset)
# -----------------------------
posts = [
    "The beach resort in Goa was amazing! Loved the view and food.",
    "Our trip to Paris was too expensive and crowded. Not enjoyable.",
    "Had a relaxing vacation in Kerala. The backwaters are beautiful.",
    "The hotel service was terrible, very disappointed with the staff.",
    "Visiting the Taj Mahal was a dream come true. Absolutely stunning!",
    "The flight was delayed for hours, ruined my holiday mood.",
    "Had the best mountain trekking experience in Himachal!",
    "Crowded tourist spots made the trip stressful.",
    "I enjoyed the local food and culture in Japan.",
    "The weather spoiled our beach vacation, very upsetting."
]

# -----------------------------
# Simple sentiment word lists
# -----------------------------
positive_words = {"amazing", "loved", "relaxing", "beautiful", "stunning",
                  "best", "dream", "enjoyed"}
negative_words = {"expensive", "crowded", "terrible", "disappointed",
                  "delayed", "ruined", "stressful", "spoiled", "upsetting"}

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)  # keep only letters and spaces
    return text.split()

def get_sentiment(tokens):
    pos = sum(1 for w in tokens if w in positive_words)
    neg = sum(1 for w in tokens if w in negative_words)
    if pos > neg:
        return "positive"
    elif neg > pos:
        return "negative"
    else:
        return "neutral"

# -----------------------------
# Process posts
# -----------------------------
all_tokens = []
sentiments = []

for p in posts:
    tokens = clean_text(p)
    all_tokens.extend(tokens)
    sentiments.append(get_sentiment(tokens))

# -----------------------------
# Results
# -----------------------------
# Sentiment distribution
print("Sentiment Analysis Results:")
print("Positive:", sentiments.count("positive"))
print("Negative:", sentiments.count("negative"))
print("Neutral :", sentiments.count("neutral"))
print()

# Top keywords (ignoring common words)
ignore = {"the", "and", "was", "our", "for", "with", "had", "very"}
filtered = [w for w in all_tokens if w not in ignore and len(w) > 2]
top_words = Counter(filtered).most_common(10)

print("Top Keywords in Tourism Posts:")
for word, count in top_words:
    print(f"{word}: {count}")
