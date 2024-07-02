from examate_project import messages


class CustomAPIException(Exception):
    def __init__(self, error_code, params=None):
        self.error_code = error_code
        if error_code:
            self.message = getattr(messages, error_code)
        if params:
            if isinstance(params, (int, str)):
                params = (params,) 
            self.message = self.message.format(*params)
        self.status_code = 400
        self.response = {
            "errorCode": self.error_code,
            "message": self.message,
        }
        super().__init__(self.response)


class CandidateNotFound(CustomAPIException):
    
    def __init__(self,error_code):
        super().__init__(error_code)

class ExamNotFound(CustomAPIException):
    
    def __init__(self,error_code):
        super().__init__(error_code)


class NoExamCandidates(CustomAPIException):
    
    def __init__(self,error_code,params=None):
        super().__init__(error_code,params)