import pandas as pd
from load_data import load_products, load_reviews, load_users
from aspect_analysis import analyze_review_aspects
from recommend_helpers import get_candidate_pool


ASPECT_COLUMNS = ["battery", "camera", "screen", "display"]

def get_user_device(user_id, users_df):
    record = users_df[users_df["user_id"] == user_id]
    if record.empty:
        return None
    return record.iloc[0]["product_id"]

def get_user_review(user_id, product_id, reviews_df):
    row = reviews_df[(reviews_df["user_id"] == user_id) & (reviews_df["product_id"] == product_id)]
    if row.empty:
        return None
    return row.iloc[0]["review_text"]

def recommend_by_aspects(user_id, top_k=3):
    products_df = load_products()
    reviews_df = load_reviews()
    users_df = load_users()

    # 1. 找出使用者購買的手機
    user_phone_id = get_user_device(user_id, users_df)
    if user_phone_id is None:
        return {}

    user_phone = products_df[products_df["product_id"] == user_phone_id].iloc[0]
    print(f"📱 User {user_id} purchased {user_phone['name']}")

    # 2. 找出該手機的評論，分析面向情緒
    review_text = get_user_review(user_id, user_phone_id, reviews_df)
    if not review_text:
        return {}
    
    aspect_sentiments = analyze_review_aspects(review_text)
    if not aspect_sentiments:
        return {}

    

    # 3. 過濾候選手機（排除使用者自己買的）
    candidates = products_df[products_df["product_id"] != user_phone_id].copy()
    recommendations = {}

    for aspect, sentiment in aspect_sentiments:
        if aspect not in ASPECT_COLUMNS:
            continue

        user_value = user_phone[aspect]
        pool = get_candidate_pool(aspect, sentiment, user_value, candidates)

        if pool.empty:
            continue

        pool["price_diff"] = abs(pool["price"] - user_phone["price"])
        top_recs = pool.sort_values("price_diff").head(top_k)
        recommendations[aspect] = top_recs[["product_id", "name", aspect, "price"]]

        # Debug 用
        print(f"[DEBUG] aspect={aspect} | sentiment={sentiment} | user spec = {user_value}")
        print(pool[["product_id", "name", aspect, "price", "price_diff"]])


    return recommendations
