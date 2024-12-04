import pandas as pd


file_paths = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]


data_frames = []

for file_path in file_paths:
    
    df = pd.read_csv(file_path)
    
   
    df = df[df["product"] == "pink morsel"]
    
    
    df["sales"] = df["quantity"] * df["price"]
    
   
    df = df[["sales", "date", "region"]]
    
    
    data_frames.append(df)


final_data = pd.concat(data_frames, ignore_index=True)


output_file = "formatted_sales_data.csv"
final_data.to_csv(output_file, index=False)


