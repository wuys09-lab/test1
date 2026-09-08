# auth.py
"""模拟登录页面的后端校验逻辑"""


class AuthenticationError(Exception):
    """认证失败：用户名或密码错误"""
    pass


class ValidationError(Exception):
    """参数校验失败"""
    pass


def login(username: str, password: str) -> dict:
    """
    模拟登录接口
    - 成功返回 token
    - 各种异常分支用于演示测试覆盖
    """
    # 1. 类型校验
    if not isinstance(username, str) or not isinstance(password, str):
        raise TypeError("Username and password must be strings")

    # 2. 空值校验
    if username.strip() == "" or password.strip() == "":
        raise ValidationError("Username and password cannot be empty")

    # 3. 长度边界校验（假设最大 50 字符）
    if len(username) > 50 or len(password) > 50:
        raise ValidationError("Username or password exceeds 50 characters")

    # 4. 模拟认证逻辑
    if username == "admin":
        if password == "Admin@123":
            return {
                "status": "success",
                "user_id": 1,
                "token": "mock_jwt_token_xyz"
            }
        else:
            raise AuthenticationError("Invalid password")
    else:
        raise AuthenticationError("User not found")