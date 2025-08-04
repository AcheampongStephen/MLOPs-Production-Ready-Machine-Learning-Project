from us_visa.logger import logging
from us_visa.exception import USVisaException
import sys



#logging.info("Logging is set up successfully.")


try:
    a = 1 / 0
except Exception as e:
    logging.error(f"An error occurred: {e}")
    raise USVisaException(e, sys) from e