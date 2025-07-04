from dataclasses import dataclass
from torch.utils.data.dataloader import DataLoader

@dataclass
class dataIngestionAtifact:
    train_file_path:str
    test_file_path:str