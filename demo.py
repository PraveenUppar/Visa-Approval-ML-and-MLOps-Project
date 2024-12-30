# from us_visa.logger import logger
# from us_visa.exception import USvisaException

# logging.info("Welcome to custom logging")

'''
try: 
    a = 1/0
except Exception as e:
    raise USvisaException(e,sys)
'''

from us_visa.pipline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()






