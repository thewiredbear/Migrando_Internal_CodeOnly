from migrandoLeadScore.config.configuration import ConfigurationManager
from migrandoLeadScore.conponents.data_preprocessing import DataPreProcess
from migrandoLeadScore.logging import logger


class DataPreProcessTrainingPipeline:
    def __init__(self):
        pass

    def main_data(self,df):
        data_preprocess = DataPreProcess()
        data_frame = data_preprocess.preprocess_data(df=df)
        return data_frame

    def main_dataframe(self,df):
        data_preprocess = DataPreProcess()
        data_frame = data_preprocess.validate_dataframe(df=df)
        return data_frame        