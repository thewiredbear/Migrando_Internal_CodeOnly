from dataclasses import dataclass
from pathlib import Path
from typing import Optional

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL:str


@dataclass(frozen=True)
class ModelTrainerConfig:
    target: str
    ignore_features: Optional[list] = None
    train_size: float = 0.7
    preprocess: bool = True
    max_encoding_ohe: int = 1
    encoding_method: str = 'encoder'
    normalize: bool = True
    normalize_method: str = 'minmax'
    feature_selection: bool = True
    feature_selection_method: str = 'univariate'
    n_features_to_select: float = 0.25
    sort: str= 'F1'
    cross_validation: bool = True
    probability_threshold: float =0.075

