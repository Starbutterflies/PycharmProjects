def debug_output(func):
    def wrapper(*args, **kwargs):
        # 输出所有传递给函数的位置参数
        print("Positional arguments:", args)

        # 输出所有传递给函数的关键字参数
        print("Keyword arguments:", kwargs)

        # 记录中间变量的值
        intermediate_values = {}

        # 包装被装饰的函数，捕获中间变量的值
        def capture_variable_value(var_name):
            def capture_var(value):
                intermediate_values[var_name] = value
                return value
            return capture_var

        # 获取被装饰的函数
        original_function = func(*args, **kwargs)

        # 在每个中间变量上应用捕获函数
        for var_name in original_function.__code__.co_varnames:
            original_function.__dict__[var_name] = capture_variable_value(var_name)

        # 执行原始函数
        result = original_function(*args, **kwargs)

        # 输出中间变量的值
        print("Intermediate variable values:", intermediate_values)

        # 输出函数的返回值
        print("Result:", result)

        return result

    return wrapper

# 使用装饰器
@debug_output
def add_numbers(x, y):
    intermediate_result = x + y
    final_result = intermediate_result * 2
    return final_result

# 调用被装饰的函数
add_numbers(3, 5)
