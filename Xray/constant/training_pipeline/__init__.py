from datetime import datetime
from typing import List



TIMESTAMP :datetime = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

ARTIFACT_DIR:str = "artifacts"
BUCKET_NAME:str = "thilan-xray-data-ingestion-2025"
S3_DATA_FOLDER:str  = "xray-data"
CLASS_LABEL_1: "NORMAL"
CLASS_LABEL_2:"PNEUMONIA"
