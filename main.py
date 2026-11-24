import os

os.makedirs("/output", exist_ok=True)
joke = "I automated my job with a script. Now I spend all day maintaining the script."
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(joke)
