from migrandoLeadScore.constants import *
from migrandoLeadScore.utils.common import read_yaml, create_directories
from migrandoLeadScore.entity import (DataIngestionConfig, ModelTrainerConfig)
from migrandoLeadScore.logging import logger


class ConfigurationManager:
    def __init__(
            self,
            config_filepath=CONFIG_FILE_PATH,
            params_filepath=PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL
        )
        return data_ingestion_config


    def get_model_trainer_config(self) -> ModelTrainerConfig:
        params = self.params.TrainingArguments
        
        model_trainer_config = ModelTrainerConfig(
            target=params.target,
            ignore_features=params.ignore_features,
            train_size=params.train_size,
            preprocess=params.preprocess,
            max_encoding_ohe=params.max_encoding_ohe,
            normalize=params.normalize,
            normalize_method=params.normalize_method,
            feature_selection=params.feature_selection,
            feature_selection_method=params.feature_selection_method,
            n_features_to_select=params.n_features_to_select
        )

        return model_trainer_config

    # def get_model_evaluation_config(self) -> ModelEvaluationConfig:
    #     config = self.config.model_evaluation

    #     create_directories([config.root_dir])

    #     model_evaluation_config = ModelEvaluationConfig(
    #         root_dir=config.root_dir,
    #         data_path=config.data_path,
    #         model_path = config.model_path,
    #         tokenizer_path = config.tokenizer_path,
    #         metric_file_name = config.metric_file_name

    #     )

    #     return model_evaluation_config
