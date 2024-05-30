



import os
import category_encoders as ce
from migrandoLeadScore.entity import ModelTrainerConfig
from migrandoLeadScore.logging import logger
from pycaret.classification import *
import pandas as pd


class ModelPrediction:
    def __init__(self):
       pass


    def prepareInput(self,inputData):
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
    def predict(self ,inputData ):
        input_df = self.prepareInput(inputData=inputData,)
        input_df.drop(columns=["Id","SalesCount","1-Beratung?","1-Welches befristete AR haben Sie?","1-Test Sprache","Zeitpunkt der Erstellung","Sales","Zeitpunkt der nderung","Zeitpunkt der Erstellung - Year","Zeitpunkt der nderung - Year"], inplace=True)
        predicted_class = model.predict(input_df)
        probability = model.predict_proba(input_df)
        response = {
            'predicted_class': predicted_class,
            'probability': probability
        }

        return response