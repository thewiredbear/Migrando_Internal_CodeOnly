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
        print(self.config.source_URL)
        if os.path.exists(self.config.source_URL):
            df = pd.read_csv(self.config.source_URL)
            return df
        else:
            logger.info(f"Unable to read the file")  
