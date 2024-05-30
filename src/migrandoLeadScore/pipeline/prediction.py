from  migrandoLeadScore.utils.common import prepareInput


class ModelPredictionPipeline:
    def __init__(self,finalModel ):
        self.finalmodel = finalModel


    
    def predict(self,inputData ):
        input_df = prepareInput(inputData=inputData,)
        input_df.drop(columns=["Id", "SalesCount", "1-Beratung?", "1-Welches befristete AR haben Sie?", "1-Test Sprache", "Zeitpunkt der Erstellung",
                    "Sales", "Zeitpunkt der nderung", "Zeitpunkt der Erstellung - Year", "Zeitpunkt der nderung - Year"], inplace=True)
        predicted_class = self.finalmodel.predict(input_df)
        probability = self.finalmodel.predict_proba(input_df)
        response = {
            'predicted_class': predicted_class,
            'probability': probability
        }

        return response
