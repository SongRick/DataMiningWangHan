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
                it = iter(value['datarange'])
                tmp = random.randint(next(it), next(it))
            # float类型 给定范围内随机生成，保留小数点后2位
            elif key == "float":
                it = iter(value['datarange'])
                tmp = round(random.uniform(next(it), next(it)),2)
            # string类型 给定范围内随机生成指定数目的字符
            elif key == "str":
                tmp = ''.join(random.SystemRandom().choice(value['datarange']) for _ in range(value['len']))
            # 自定义类型 递归处理
            else:
                tmp=struct_data_sampling(1, **value)
            element.append(tmp)
        result.append(element)
    return result
def apply():
    """
    自定义了一个数据结构:
    学校
        学校编号(int)
        班级
            班级编号(int)
            学生
                学生学号(int)
                姓名(str)
    """
    school={
        "int":{"datarange": (0, 10)},
        "class":{
            "int":{"datarange":(11,20)},
            "student":{
                "int": {"datarange": (2024001, 2024100)},
                "str":{
                    "datarange": string.ascii_uppercase,
                    "len": 5
                }
            }
        }
    }
    result = struct_data_sampling(2, **school)
    print(result)
if __name__ == "__main__":
    apply()