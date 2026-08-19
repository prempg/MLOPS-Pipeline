from src.data_ingestion import main as data_ingestion_main
from src.data_preprocessing import main as data_preprocessing_main
from src.loggers import logger


def main():
    try:
        logger.info("Starting MLOps pipeline")

        # Step 1: Data Ingestion
        logger.info("Starting data ingestion")
        data_ingestion_main()
        logger.info("Data ingestion completed successfully")

        # Step 2: Data Preprocessing
        logger.info("Starting data preprocessing")
        data_preprocessing_main()
        logger.info("Data preprocessing completed successfully")

        logger.info("MLOps pipeline completed successfully")

    except Exception as e:
        logger.error("MLOps pipeline failed: %s", e)
        raise


if __name__ == "__main__":
    main()