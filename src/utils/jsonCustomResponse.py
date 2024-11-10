def jsonCustomResponse(code: int, message: str, data: any):
    return {
        "code": code,
        "message": message,
        "data": data
    }