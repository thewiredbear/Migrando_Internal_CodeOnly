from migrandoLeadScore.config.configuration import ConfigurationManager
from migrandoLeadScore.conponents.model_trainer import ModelTrainer
from migrandoLeadScore.logging import logger
import category_encoders as ce


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self, dataframe):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        encoder = ce.GLMMEncoder()
        trained_model = model_trainer_config.train(
            encoder=encoder, df=dataframe)
        trained_model.get_config("train")
        model = trained_model.create_model('qda', cross_validation=model_trainer_config.config.cross_validation,
                                           probability_threshold=model_trainer_config.config.probability_threshold)
        toBePredict_dataframe = dataframe.copy()
        trained_model.predict_model(model, data=toBePredict_dataframe)
        trained_model = trained_model.finalize_model(model)
        return {"trainedModel": trained_model, "model": model}
        # init_model = trained_model.compare_models(sort=model_trainer_config.config.sort,
        # cross_validation=model_trainer_config.config.cross_validation,
        # probability_threshold=model_trainer_config.config.probability_threshold)
