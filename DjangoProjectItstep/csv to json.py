import csv
import datetime
import json

with open("js.json", "r") as f:
    all_js = json.load(f)
with open("ITStep/vgsales.csv") as f:
    all_info = csv.reader(f)
    try:
        for i in all_info:
            all_js.append(
                {
                    "name": i[1],
                    "platform": i[2],
                    "year": i[3],
                    "genre": i[4],
                    "publisher": i[5],
                    "na_sales": i[6],
                    "eu_sales": i[7],
                    "jp_sales": i[8],
                    "other_sales": i[9],
                    "global_sales": i[10],
                }
            )
    except:
        pass
with open("js.json", "w") as file:
    json.dump(all_js, file, indent=4)
