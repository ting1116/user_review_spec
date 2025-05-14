import pandas as pd

def generate_reason_table(recommendations: dict, explanations: dict) -> pd.DataFrame:
    """
    整合推薦結果與推薦理由，生成清楚的表格。
    
    每列包含：
    - 推薦產品資料（如 battery, camera, price）
    - 面向（aspect）
    - 推薦理由（reason）
    """
    rows = []

    for aspect in recommendations:
        recs = recommendations[aspect]
        expls = explanations[aspect]

        for i in range(len(recs)):
            row = recs.iloc[i].to_dict()
            row["aspect"] = aspect
            row["reason"] = expls[i]
            rows.append(row)

    table_df = pd.DataFrame(rows)
    return table_df
