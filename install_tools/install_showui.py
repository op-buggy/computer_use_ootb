import os
from modelscope.hub.snapshot_download import snapshot_download

# Specify the model repository and destination folder
model_repo = "AI-ModelScope/ShowUI-2B"
destination_folder = "./showui-2b/"

# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Download the model using ModelScope
print(f"开始从 ModelScope 下载模型 {model_repo}...")
model_path = snapshot_download(model_repo, local_dir=destination_folder)
print(f"模型已下载到: {model_path}")

# 移动文件到正确位置
import shutil
import glob

# 获取下载的模型文件路径
model_files = glob.glob(os.path.join(model_path, "*"))
# 移动所有文件到目标目录
for file in model_files:
    shutil.move(file, destination_folder)
# 删除空的原始目录
shutil.rmtree(model_path)