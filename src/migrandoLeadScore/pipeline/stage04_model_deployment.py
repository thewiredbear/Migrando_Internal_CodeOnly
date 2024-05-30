import category_encoders as ce
import modelbit
from migrandoLeadScore.config.configuration import ConfigurationManager
from migrandoLeadScore.conponents.model_trainer import ModelTrainer
from migrandoLeadScore.logging import logger
import category_encoders as ce
from  migrandoLeadScore.utils.common import prepareInput
from migrandoLeadScore.constants import user_input

class ModelDeploymentPipeline:
    def __init__(self,finalModel , model):
        self.finalmodel = finalModel
        self.model = model
    
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
    def main(self):
        # config = ConfigurationManager()
        # model_trainer_config = config.get_model_trainer_config()
        # model_trainer_config = ModelTrainer(config=model_trainer_config)
        # encoder = ce.GLMMEncoder()
        # trained_model = model_trainer_config.train(
        #     encoder=encoder, df=dataframe)
        # trained_model.get_config("train")
        # model = trained_model.create_model('qda', cross_validation=model_trainer_config.config.cross_validation,
        #                                    probability_threshold=model_trainer_config.config.probability_threshold)
        # toBePredict_dataframe = dataframe.copy()
        # trained_model.predict_model(model, data=toBePredict_dataframe)
        # trained_model = trained_model.finalize_model(model)
        md=modelbit.login()
        md.add_model("leadScore",self.model)
        md.deploy(self.predict)