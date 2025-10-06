import os
import pandas as pd

df = pd.read_csv("rename_files.csv")
folder_path = "//rename_test_folder"

for index, row in df.iterrows():
    old_file = os.path.join(folder_path, row['old_name'])
    new_file = os.path.join(folder_path, row['new_name'])

    try:
        if os.path.exists(old_file):
            os.rename(old_file, new_file)
            print(f"Renamed {row['old_name']} to {row['new_name']}")
        else:
            print(f"File {row['old_name']} not found.")
    except Exception as e:
        print(f"Error renaming {row['old_name']}: {e}")