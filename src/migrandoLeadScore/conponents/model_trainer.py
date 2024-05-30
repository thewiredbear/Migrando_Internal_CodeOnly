import os
import category_encoders as ce
from migrandoLeadScore.entity import ModelTrainerConfig
from migrandoLeadScore.logging import logger
from pycaret.classification import *

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    
    def train(self , encoder , df ):
        train = setup(df,
        target = self.config.target,
        ignore_features =self.config.ignore_features ,
        train_size=self.config.train_size ,
        preprocess=self.config.preprocess ,
        max_encoding_ohe=self.config.max_encoding_ohe,
        encoding_method=encoder,
        normalize=self.config.normalize,
        normalize_method=self.config.normalize_method,
        feature_selection=self.config.feature_selection,
        feature_selection_method=self.config.feature_selection_method,
        n_features_to_select=self.config.n_features_to_select
        )
        return train
