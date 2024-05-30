import os
from migrandoLeadScore.logging import logger
from migrandoLeadScore.utils.common import remove_non_ascii
import pandas as pd

class DataPreProcess:

    def preprocess_data(self, df) -> bool:
        try:
            new_df = df[['Abschluss', 'Abschluss_in_DE', 'Deutscher_Ehepartner', 'EB_NE_erf_llt', 'Einreisejahr', 'Haben_Sie_bereits_einen_Antrag_auf_Einb_rgerung_ge', 'Haben_Sie_bereits_einen_Antrag_auf_ein_unbefristet', 'Integrationstest',
                         'Jahr_AR_beantragt_bekommen', 'Jobcenter', 'Kinder', 'Netto', 'Rente', 'Sprachzertifikat1', 'Test_Sprache', 'Welches_befristete_AR_haben_Sie', 'Wie_ist_ihr_aktueller_Familienstand', 'Beratung', 'G_ltiger_Nationalpass', 'id', 'Sales']]
            new_df.columns = ['1-Abschluss', '1-Abschluss in DE', '1-Deutscher Ehepartner', '1-EB/NE erfllt?', '1-Einreisejahr', '1-Antrag EB', '1-Antrag NE', '1-Integrationstest', '1-Jahr AR beantragt/bekommen', '1-Jobcenter',
                              '1-Kinder', '1-Netto', '1-Rente', '1-Sprachzertifikat', '1-Test Sprache', '1-Welches befristete AR haben Sie?', '1-Wie ist ihr aktueller Familienstand?', '1-Beratung?', '1-Gltiger Nationalpass', 'Id', 'Sales']
            temp_df = new_df
            temp_df["Sales"] = temp_df["Sales"].astype('int64')
            temp_df["SalesCount"] = temp_df["Sales"].apply(
                lambda x: 1 if x > 0 else 0)
            temp_df["SalesCount"] = temp_df["SalesCount"].astype('int64')
            temp_df = temp_df.dropna(subset=["Sales"])
            temp_df = temp_df[temp_df["1-Abschluss"] != ""]
            replace_values_dict = {
                "1-Abschluss in DE": {"": "Not Asked"},
                "1-Deutscher Ehepartner": {"": "Not Asked"},
                "1-Einreisejahr": {"Vor 2014": "Vor 2015", "2011 oder davor": "Vor 2015", "2012": "Vor 2015", "2013": "Vor 2015", "2014": "Vor 2015"},
                "1-Jahr AR beantragt/bekommen": {"Vor 2014": "Vor 2015", "2014": "Vor 2015", "": "Not Asked"},
                "1-Jobcenter": {"": "Not Asked"},
                "1-Rente": {"": "Not Asked"},
                "1-Sprachzertifikat": {"": "Not Asked"},
                "1-Test Sprache": {"": "Deutsch"}
            }
            temp_df.replace(replace_values_dict, inplace=True)
            temp_df = temp_df[temp_df["1-Antrag EB"] != ""]
            temp_df = temp_df[temp_df["1-Beratung?"].isin(["Ja", "Nein"])]
            temp_df = temp_df[temp_df["1-Welches befristete AR haben Sie?"] != ""]
            temp_df = temp_df.applymap(remove_non_ascii)
            return temp_df
        except Exception as e:
            raise e

    def validate_dataframe(self, df) -> bool:
        try:
            df_filtered = df[df['1-Beratung?'] != 'Nein']
            return df_filtered
        except Exception as e:
            raise e

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
