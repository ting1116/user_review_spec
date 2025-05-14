from pathlib import Path

# 專案根目錄
PROJECT_ROOT = Path(r"C:\YuTingWeng\Graduate\113-2\1132_database_system\final_project\user_review_spec_based_rec")

# 資料夾
DATA_DIR = PROJECT_ROOT / "data"

# 資料檔案路徑
PRODUCTS_CSV = DATA_DIR / "products.csv"
REVIEWS_CSV = DATA_DIR / "reviews.csv"
USERS_CSV = DATA_DIR / "users.csv"

# 用法
# import pandas as pd
# from config import PRODUCTS_CSV, REVIEWS_CSV, USERS_CSV
# df_products = pd.read_csv(PRODUCTS_CSV)
# print(df_products.head())