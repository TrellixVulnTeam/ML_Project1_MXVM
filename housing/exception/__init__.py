import sys
import os



class HousingException(Exception):
    
    def __init__(self,error_message:Exception, error_detail = sys):
        super().__init__(error_message)
        
        self.error_message = error_message


