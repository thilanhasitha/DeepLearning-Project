# import os
# import sys

# def error_message_detail(error:Exception,error_detail:sys)-> str:
#     _,_,exc_tb = error_detail.exc_info()

#     file_name:str = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

#     error_message:str = "Error occured python script name [{0}] line number [{1}] error"
#     file_name,exc_tb.tb_lineno,str(error)
    
#     return error_message

import os
import sys

def error_message_detail(error: Exception, error_detail: sys) -> str:
    _, _, exc_tb = error_detail.exc_info()
    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    line_number = exc_tb.tb_lineno
    return f"Error occurred in script: [{file_name}] at line [{line_number}] with error: {str(error)}"

class XRayException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
