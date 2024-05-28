from migrandoLeadScore.config.configuration import ConfigurationManager
from migrandoLeadScore.conponents.data_ingestion import DataIngestion
from migrandoLeadScore.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_frame = data_ingestion.read_file()
        return data_frame