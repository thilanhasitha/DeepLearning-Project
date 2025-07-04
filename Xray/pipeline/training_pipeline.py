import sys

from Xray.components.data_ingestion import DataIngestion
from Xray.entity.artifact_entity import DataIngestionArtifact
from Xray.entity.config_entity import DataIngestionConfig
from Xray.exception import XRayException
from Xray.logger import logging

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self)->DataIngestionArtifact:
        logging.info( "Entered the start _data_ingestion method of training")

    try:
        logging.info("Getting the data from the s3 bucket")

        data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config,)

        data_ingestion_artifact = data_ingestion.initiate_data_ingestion

        logging.info("got the train set and test set from s3")
        logging.info("Existed the start_data_ingestion method of pipeline class")

        #return data_ingestion_artifact
    
    except Exception as e:
        raise XRayException(e,sys)



