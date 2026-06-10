import os

print("環境変数一覧")
print(list(os.environ.keys()))

print("ある？")
print("OPENWEATHER_KEY" in os.environ)
