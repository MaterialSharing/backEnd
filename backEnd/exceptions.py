from MySQLdb import DataError
from rest_framework.response import Response
from rest_framework.views import exception_handler

Res = Response


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    # 调用REST framework的默认异常处理程序，以便获得标准错误响应。
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response


def division_exception_handler(exc, context):
    """
    自定义异常处理程序
    :param exc: 即exception异常实例
    :type exc:
    :param context:
    :type context:
    :return:
    :rtype:
    """
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    # 调用REST framework的默认异常处理程序，以便获得标准错误响应。
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    # print("capture_exception@@@@")
    if response is None:
        if isinstance(exc, ZeroDivisionError):
            response = Res({"detail": "除数不能为0"})
        # response.data['status_code'] = response.status_code
        if isinstance(exc, DataError):
            response = Res({"detail": "数据库操作错误"})
    # 如果drf自己可以处理的异常,那么就直接返回
    # 返回处理完的(包装后的)异常信息
    return response
