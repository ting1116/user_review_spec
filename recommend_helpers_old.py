
import pandas as pd

def get_candidate_pool(aspect, sentiment, user_value, candidates):
    TOLERANCE = {
        "battery": 1200,
        "camera": 4,
        "screen": 2,
    }

    if aspect not in candidates.columns:
        return pd.DataFrame()

    # 若為不可比較型別（如字串），跳過該面向
    if isinstance(user_value, str) or candidates[aspect].dtype == object:
        return pd.DataFrame()

    if sentiment == "positive":
        delta = TOLERANCE.get(aspect, 200)
        pool = candidates[abs(candidates[aspect] - user_value) <= delta]
    elif sentiment == "negative":
        pool = candidates[candidates[aspect] > user_value]
    else:
        pool = pd.DataFrame()

    return pool.copy()
