import sys
import os
from dataclasses import dataclass
import numpy as np 
import pandas as pd 
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.exception import CustomException
from src.logger import logging 

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")

class DataTransformation:

    def __init__(self):
        self.Data_transformation_config = DataTransformationConfig()

    # this function is to create pickle file
    def get_data_transformer_object(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course"
            ]
            # create a numerical pipeline with two steps
            num_pipeline = Pipeline(
                steps=("imputer", SimpleImputer(strategy="median")
                )
            )
        except:
            pass    

