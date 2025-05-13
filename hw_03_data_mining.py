"""
数据挖掘-王晗 第三次作业 2025年5月6日
函数功能：
    1、写一个修饰器，实现 SUM、AVG、方差、RMSE，用于前述 dataSampling
"""

import random
import string
import math
import pprint


def StaticRes(*metrics):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 调用被修饰函数获取数据
            data = func(*args, **kwargs)

            # 打印生成的数据
            print("生成的数据：")
            pprint.pprint(data, indent=2)
            print("\n统计结果:")

            # 递归展开所有数值
            def flatten(items):
                flattened = []
                if isinstance(items, dict):
                    items = items.values()
                for item in items:
                    if isinstance(item, (list, tuple, dict)):
                        flattened.extend(flatten(item))
                    elif isinstance(item, (int, float)):
                        flattened.append(item)
                return flattened

            all_values = flatten(data)

            # 计算统计指标
            results = {}
            n = len(all_values)
            if n == 0:
                for metric in metrics:
                    results[metric] = None
                return results

            sum_val = sum(all_values)
            avg_val = sum_val / n
            sum_sq = sum(x ** 2 for x in all_values)
            variance = sum((x - avg_val) ** 2 for x in all_values) / (n - 1) if n > 1 else 0.0
            rmse = math.sqrt(sum_sq / n)

            # 根据参数填充结果
            for metric in metrics:
                if metric == 'SUM':
                    results['SUM'] = sum_val
                elif metric == 'AVG':
                    results['AVG'] = avg_val
                elif metric == 'VAR':
                    results['VAR'] = variance
                elif metric == 'RMSE':
                    results['RMSE'] = rmse
                else:
                    raise ValueError(f"Unsupported metric: {metric}")
            return results

        return wrapper

    return decorator


def dataSampling(num, **kwargs):
    result = []
    for _ in range(num):
        element = []
        for key, value in kwargs.items():
            if key == "int":
                dr = value['data_range']
                tmp = random.randint(dr[0], dr[1])
            elif key == "float":
                dr = value['data_range']
                dp = value.get('decimal_places', 2)
                tmp = round(random.uniform(dr[0], dr[1]), dp)
            elif key == "str":
                chars = value['data_range']
                length = value['len']
                tmp = ''.join(random.choices(chars, k=length))
            else:
                # 递归处理嵌套结构
                tmp = dataSampling(1, **value)[0]
            element.append(tmp)
        result.append(element)
    return result


# 应用修饰器
@StaticRes('SUM', 'AVG', 'VAR', 'RMSE')
def decorated_dataSampling(*args, **kwargs):
    return dataSampling(*args, **kwargs)


# 测试代码
if __name__ == "__main__":
    entry = {
        "int": {"data_range": (1, 10)},
        "float": {"data_range": (0, 100), "decimal_places": 2},
        "student_participant": {
            "str": {"data_range": string.ascii_uppercase, "len": 2},
            "int": {"data_range": (2024001, 2024999)},
            "advisor": {
                "str": {"data_range": string.ascii_uppercase, "len": 3},
                "contact_information": {
                    "int": {"data_range": (1000000, 9999999)},
                    "str": {"data_range": string.ascii_lowercase, "len": 15}
                }
            }
        }
    }

    # 生成数据并计算统计指标
    stats = decorated_dataSampling(num=5, **entry)
    print(stats)
