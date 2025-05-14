user_review_spec_based_rec/
├── data/
│   ├── products.csv          # 手機規格與描述資料
│   ├── reviews.csv           # 使用者評論資料
│   ├── users.csv             # 會員購買紀錄
├── config.py                 # 資料路徑控制設定
├── load_data.py              # 載入與預處理資料
├── recommend.py              # 推薦主邏輯（規格 + 評價）
├── aspect_analysis.py        # 面向與情緒分析模組
├── explain.py                # 結果解釋模組（推薦理由）
├── graph_export.py           # 推薦理由圖譜 NetworkX 輸出
├── demo.ipynb                # 互動式展示與測試範例
