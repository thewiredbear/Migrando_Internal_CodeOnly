import os
from box.exceptions import BoxValueError
import yaml
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import modin.pandas as pd

from migrandoLeadScore.logging import logger

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def prepareInput(inputData):
    try:
        """
        Prepare a DataFrame from input data to match the structure of the training data.
        """
        # Define the columns as per the original DataFrame
        columns = [
            "1-Abschluss", "1-Abschluss in DE", "1-Deutscher Ehepartner", "1-EB/NE erfllt?", "1-Einreisejahr",
            "1-Antrag EB", "1-Antrag NE", "1-Integrationstest", "1-Jahr AR beantragt/bekommen", "1-Jobcenter",
            "1-Kinder", "1-Netto", "1-Rente", "1-Sprachzertifikat", "1-Test Sprache",
            "1-Welches befristete AR haben Sie?", "1-Wie ist ihr aktueller Familienstand?", "1-Beratung?",
            "1-Gltiger Nationalpass", "Id", "Zeitpunkt der Erstellung", "Sales", "Zeitpunkt der nderung",
            "Zeitpunkt der Erstellung - Year", "Zeitpunkt der nderung - Year", "SalesCount"
        ]

        # Create a DataFrame with the input data
        input_df = pd.DataFrame([inputData], columns=columns)
        return input_df
    except Exception as e:
        raise e




def remove_non_ascii(text):
    return ''.join(char for char in text if ord(char) < 128)
