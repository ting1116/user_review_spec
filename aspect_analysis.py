from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# 初始化情緒分析工具
analyzer = SentimentIntensityAnalyzer()

# 手動定義常見面向關鍵字（可依產品類型擴充）
ASPECT_KEYWORDS = ["battery", "camera", "screen", "display", "performance", "charging"]

def analyze_review_aspects(review_text):
    """
    輸入：review_text（字串）
    輸出：List of (aspect, sentiment) tuples，例如：
        [("battery", "negative"), ("camera", "positive")]
    """
    results = []
    text_lower = review_text.lower()
    for aspect in ASPECT_KEYWORDS:
        if aspect in text_lower:
            score = analyzer.polarity_scores(review_text)["compound"]
            sentiment = (
                "positive" if score > 0.2 else
                "negative" if score < -0.2 else
                "neutral"
            )
            results.append((aspect, sentiment))
    return results

# 單元測試
if __name__ == "__main__":
    sample_reviews = [
        "Battery drains too fast, but the camera is amazing.",
        "The screen is sharp, but performance is laggy.",
        "I love the display and battery life.",
        "Camera quality is mediocre."
    ]
    for text in sample_reviews:
        print(f"\n📄 Review: {text}")
        print(analyze_review_aspects(text))

# 這段程式碼使用 VADER 進行情緒分析，並根據定義的面向關鍵字來分析評論的情緒。
# 使用方式
# from aspect_analysis import analyze_review_aspects
# text = "Battery drains too fast, but the camera is amazing"
# print(analyze_review_aspects(text))
# # ➜ [('battery', 'negative'), ('camera', 'positive')]