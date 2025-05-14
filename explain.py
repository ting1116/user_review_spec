from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def extract_good_reviews_by_aspect(product_id, aspect, reviews_df, sentiment_threshold=0.3):
    """
    擷取其他使用者針對某面向的好評句
    """
    matched_reviews = reviews_df[
        (reviews_df["product_id"] == product_id) &
        (reviews_df["review_text"].str.contains(aspect, case=False))
    ]

    good_reviews = []
    for _, row in matched_reviews.iterrows():
        text = row["review_text"]
        score = analyzer.polarity_scores(text)["compound"]
        if score > sentiment_threshold and not any(w in text.lower() for w in ["but", "however", "although"]):
            good_reviews.append(text)

    return good_reviews


def generate_explanations(user_phone, recommendations, reviews_df):
    """
    根據推薦結果與評論，產生推薦理由：規格比較 + 他人正評句子
    """
    explanations = {}

    for aspect, recs in recommendations.items():
        reason_list = []

        for _, row in recs.iterrows():
            product_id = row["product_id"]
            product_name = row["name"]
            rec_value = row[aspect]
            user_value = user_phone[aspect]

            # ➤ 規格比較說明
            if rec_value > user_value:
                reason = f"{product_name} 的 {aspect} 表現更佳（{rec_value} > {user_value}）"
            elif abs(rec_value - user_value) <= 200:
                reason = f"{product_name} 的 {aspect} 表現與你目前使用的手機相近（{rec_value} ≈ {user_value}）"
            else:
                reason = f"{product_name} 的 {aspect} 有差異"

            # ➤ 擷取其他使用者針對該面向的好評評論
            good_reviews = extract_good_reviews_by_aspect(product_id, aspect, reviews_df)

            if good_reviews:
                reason += f"，其他人評論：「{good_reviews[0]}」"

            reason_list.append(reason)

        explanations[aspect] = reason_list

    return explanations
