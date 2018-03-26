import sys


class ErrorHandler(object):

    @classmethod
    def get_error(cls):
        '''
        Retrieves the last error that happened in the current execution via the traceback library
        and returns it.
        :return:
        exc_value: str
        the information of the last error that happened in the current execution.
        '''
        exc_type, exc_value, exc_traceback = sys.exc_info()
        return str(exc_value)