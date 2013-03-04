#coding=utf-8
''' 共用方法 '''

def row2dict(row_obj):
    ''' Covert sqlalchemy row object to python dict '''
    result = {}
    for column in row_obj.__table__.columns:
        result[column.name] = getattr(row_obj, column.name)

    return result
