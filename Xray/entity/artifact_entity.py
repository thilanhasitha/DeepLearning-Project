from dataclasses import dataclass
from torch.utils.data.dataloader import DataLoader
#from Xray.entity.artifact_entity import DataIngestionArtifact  # <-- This is PascalCase


@dataclass
# artifact_entity.py
class DataIngestionArtifact:
    def __init__(self, train_file_path, test_file_path):
        self.train_file_path = train_file_path
        self.test_file_path = test_file_path
    
    def __str__(self):
        return f"Train File: {self.train_file_path}, Test File: {self.test_file_path}"