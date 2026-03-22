# ./app/spam.py
def check_spam(text: str) -> str:
    text = text.lower().strip()
    if text == "":
        return "ham"
    
    spam_keywords = [
        "free", "win", "winner", "prize", "click",
        "buy now", "urgent", "cash", "money", "offer", "deal"
    ]
    hit = 0
    for kw in spam_keywords:
        print(kw, text)
        if kw in text:
            hit += 1
    return "spam" if hit >= 2 else "ham", hit