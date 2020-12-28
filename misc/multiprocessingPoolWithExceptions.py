import multiprocessing
import traceback
from multiprocessing.pool import Pool as _Pool


def error(msg, *args):
    return multiprocessing.get_logger().error(msg, *args)


class LogExceptions(object):
    def __init__(self, _callable):
        self.__callable = _callable

    def __call__(self, *args, **kwargs):
        try:
            result = self.__callable(*args, **kwargs)

        except Exception as e:
            error(traceback.format_exc())

            raise

        return result


class Pool(_Pool):
    def apply_async(self, func, args=(), kwds={}, callback=None):
        return _Pool.apply_async(self, LogExceptions(func), args, kwds, callback)
