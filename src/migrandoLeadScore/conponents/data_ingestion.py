import os
import urllib.request as request
import pandas as pd
import zipfile
from migrandoLeadScore.logging import logger
from migrandoLeadScore.utils.common import get_size
from pathlib import Path
from migrandoLeadScore.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def read_file(self):
        if not os.path.exists(self.config.root_dir):
            df = pd.read_csv(self.config.root_dir)
            df.head(2)
            return df
        else:
            logger.info(f"Unable to read the file")  
