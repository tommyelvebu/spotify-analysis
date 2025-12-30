import kagglehub
from pathlib import Path
import shutil


def download_spotify_dataset():
    kaggle_path = Path(
        kagglehub.dataset_download("aliiihussain/spotify-analysis-and-visualization")
    )

    print("Kaggle cache path:", kaggle_path)
    
    # our project data folder which lives in data/, so parent is project root
    project_root = Path(__file__).resolve().parents[1]
    local_data_dir = project_root / "data" / "raw"
    local_data_dir.mkdir(parents=True, exist_ok=True)

    for csv_file in kaggle_path.rglob("*.csv"):
        dest = local_data_dir / csv_file.name
        shutil.copy(csv_file, dest)
        print(f"Copied {csv_file} to {dest}")
    
    print("Local data directory:", local_data_dir)
    return local_data_dir


