import json
from pathlib import Path
import os
def xuLyKetQua(**kwargs):
    data_dir = Path('checkpoints_dir')
    data_dir.mkdir(parents=True, exist_ok=True)
    file_path  = data_dir / "model_cfg.json"
    with open(file_path, "w") as f:
        json.dump(kwargs, f, indent=4)
    print(f"Đã lưu cấu hình vào: {file_path}")
if __name__ == "__main__":
    config = {"model": "ResNet", "epochs": 50, "batch_size": 32}
    xuLyKetQua(**config)