import os
from datetime import datetime
from torch import device
from Xray.constant.training_pipeline import *

# @dataclass
# class DataIngestionConfig:
#     def __init__(self):
#         self.S3_data_folder:str = S3_DATA_FOLDER
#         self.bucket_name:str = BUCKET_NAME
#         self.artifact:str = os.path.join(ARTIFACT_DIR,TIMESTAMP)
#         self.data_path:str = os.path.join(self.artifact_dir,"data ingestion",self.S3_data_folder)

#         self.train_data_path:str = os.path.join(self,data_path,"train")
#         self.test_data_path:str = os.path.join(self,data_path,"test")

import os
from datetime import datetime

class DataIngestionConfig:
    def __init__(self):
        # ✅ Step 1: Define artifact_dir first
        current_time_stamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        self.artifact_dir = os.path.join(os.getcwd(), "artifacts", current_time_stamp)

        self.bucket_name = "thilan-xray-data-ingestion-2025"

        # ✅ Step 2: Define S3 folder name
        self.S3_data_folder = "xray-data"  # change as needed

        # ✅ Step 3: Now this will work correctly
        self.data_path = os.path.join(self.artifact_dir, "data_ingestion", self.S3_data_folder)

        self.train_data_path = os.path.join(self.data_path, "train")  # example paths
        self.test_data_path = os.path.join(self.data_path, "test")


    
