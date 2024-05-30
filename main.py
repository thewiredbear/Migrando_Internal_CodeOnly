
from migrandoLeadScore.pipeline.prediction import ModelPredictionPipeline
from migrandoLeadScore.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from migrandoLeadScore.logging import logger
from migrandoLeadScore.pipeline.stage02_data_preprocess import DataPreProcessTrainingPipeline
from migrandoLeadScore.pipeline.stage03_model_trainer import ModelTrainerTrainingPipeline
from migrandoLeadScore.constants import user_input
import modelbit

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    df = data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
if not df.empty:
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        data_validation = DataPreProcessTrainingPipeline()
        df = data_validation.main_dataframe(df=df)
        logger.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model = model_trainer.main(dataframe=df)
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Prediction stage"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_predictor = ModelPredictionPipeline()
    prediction = model_predictor.predict(
        model=model["trainedModel"], inputData=user_input)
    logger.info(f">>>>>> prediction {prediction} <<<<<<\n\nx==========x")
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

try:
    user_input = input("Do you want to deploy? (y/n): ").strip().lower()
    if user_input == 'y':

        STAGE_NAME = "Model Deployment stage"
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        predictor = ModelPredictionPipeline(finalModel=model["trainedModel"])
        md=modelbit.login()
        md.add_model("leadScore",model["model"],)
        md.deploy(model_predictor.predict, skip_extra_files_dependencies=True,)
        # model_deploy = ModelDeploymentPipeline(finalModel=model["trainedModel"] , model=model["model"])
        # model_deploy.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    else:
        print("bad")
except Exception as e:
    logger.exception(e)
    raise e
