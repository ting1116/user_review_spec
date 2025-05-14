import pandas as pd
from config import PRODUCTS_CSV, REVIEWS_CSV, USERS_CSV

def load_products():
    """讀取手機產品資料"""
    return pd.read_csv(PRODUCTS_CSV)

def load_reviews():
    """讀取使用者評論資料"""
    return pd.read_csv(REVIEWS_CSV)

def load_users():
    """讀取會員購買紀錄"""
    return pd.read_csv(USERS_CSV)

if __name__ == "__main__":
    print("*Products:")
    print(load_products().head(), "\n")
    
    print("*Reviews:")
    print(load_reviews().head(), "\n")
    
    print("*Users:")
    print(load_users().head())

# 使用方法, 例如在 demo.ipynb 或其他 script 中
# 這樣就可以統一管理所有資料的載入，不需每次都寫 pd.read_csv("...")
# from load_data import load_products, load_reviews, load_users
# products_df = load_products()
# reviews_df = load_reviews()
# users_df = load_users()