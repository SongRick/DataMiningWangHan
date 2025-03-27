"""
数据挖掘-王晗 第二次作业 2025年3月25日
函数功能：
    1、生成随机数据
    2、传入参数包括生成随机数据的数量和字典格式的数据结构（即说明书）
    3、自定义数据结构，不论结构如何，函数都能正确接收和实例化
    4、最终返回一个列表，包含正确数量的数据
    5、旨在理解python动态参数的灵活性
    6、提示：递归处理嵌套数据    
"""
import random
import string

def struct_data_sampling(num, **kwargs):
    result = list()
    for index in range(0, num):
        element = list()
        for key, value in kwargs.items():
            # int类型 给定范围内随机生成
            if key == "int":
                it = iter(value['data_range'])
                tmp = random.randint(next(it), next(it))
            # float类型 给定范围内随机生成，指定保留小数点位数
            elif key == "float":
                it = iter(value['data_range'])
                decimal_places = value.get('decimal_places')
                tmp = round(random.uniform(next(it), next(it)),decimal_places)
            # string类型 给定范围内随机生成指定数目的字符
            elif key == "str":
                len=range(value['len'])
                tmp = ''.join(random.SystemRandom().choice(value['data_range']) for _ in len)
            # 自定义类型 递归处理
            else:
                tmp=struct_data_sampling(1, **value)
            element.append(tmp)
        result.append(element)
    return result
def entry():
    """
    自定义数据结构:
    参赛作品
        作品编号(int)
        作品得分(float)
        参赛学生
            学生姓名(str)
            学号(int)
            指导教师
                教师姓名(str)
                联系方式
                    电话(int)
                    地址(str)
    """
    entry={
        "int":{"data_range":(1,10)},
        "float":{"data_range":(0,100),"decimal_places":2},
        "student_participant":{
            "str": {"data_range": string.ascii_uppercase,"len": 2},
            "int": {"data_range": (2024001, 2024999)},
            "advisor":{
                "str": {"data_range": string.ascii_uppercase, "len": 3},
                "contact_information":{
                    "int":{"data_range":(1000000,9999999)},
                    "str": {"data_range": string.ascii_lowercase,"len": 15}
                }
            }
        }
    }
    result = struct_data_sampling(5, **entry)
    for element in result:
        print(element)
if __name__ == "__main__":
    entry()
