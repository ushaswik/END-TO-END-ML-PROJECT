
import sys
import logging
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in script [{0}] at line [{1}] -> [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        formatted_message = error_message_detail(error_message, error_detail)
        super().__init__(formatted_message)  # Pass formatted message to Exception
        self.error_message = formatted_message

    def __str__(self):
        return self.error_message

# # Testing the Exception Handling
# if __name__ == "__main__":
#     try:
#         a = 1 / 0
#     except Exception as e:
#         logging.info("Divide by zero error")
#         raise CustomException(e, sys)
