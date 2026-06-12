import os
import scratchattach as scratch3

print("ログイン開始")

session = scratch3.login(
    os.environ["SCRATCH_USERNAME"],
    os.environ["SCRATCH_PASSWORD"]
)

print("ログイン成功")
