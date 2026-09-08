# test_auth.py
import pytest
from auth import login, AuthenticationError, ValidationError


# ==================== Fixtures ====================

@pytest.fixture
def valid_user():
    """正常用户数据"""
    return {"username": "admin", "password": "Admin@123"}


@pytest.fixture
def invalid_users():
    """异常用例数据集（用于参数化）"""
    return [
        # (username, password, expected_exception)
        ("admin", "wrong_password", AuthenticationError),
        ("guest", "Admin@123", AuthenticationError),
        ("", "Admin@123", ValidationError),
        ("admin", "", ValidationError),
        ("   ", "Admin@123", ValidationError),
        ("admin", "   ", ValidationError),
    ]


@pytest.fixture
def boundary_cases():
    """边界值测试数据"""
    return [
        # 51 字符（超长）
        ("a" * 51, "Admin@123", ValidationError),
        ("admin", "b" * 51, ValidationError),
        # 刚好 50 字符（边界）
        ("a" * 50, "Admin@123", AuthenticationError),  # 用户不存在
        ("admin", "A" * 50, AuthenticationError),      # 密码错误
    ]


# ==================== 正常情况测试 ====================

def test_login_success(valid_user):
    """测试正常登录流程"""
    result = login(valid_user["username"], valid_user["password"])
    assert result["status"] == "success"
    assert "token" in result
    assert result["user_id"] == 1


# ==================== 参数化异常测试 ====================

@pytest.mark.parametrize("username, password, expected_exc", [
    ("admin", "wrong_password", AuthenticationError),
    ("nonexistent", "Admin@123", AuthenticationError),
    ("", "Admin@123", ValidationError),
    ("admin", "", ValidationError),
])
def test_login_authentication_failures(username, password, expected_exc):
    """测试认证失败的各种情况"""
    with pytest.raises(expected_exc):
        login(username, password)


# ==================== 边界值测试 ====================

@pytest.mark.parametrize("username, password, expected_exc", [
    ("a" * 51, "Admin@123", ValidationError),   # 超长用户名
    ("admin", "b" * 51, ValidationError),        # 超长密码
    ("a" * 50, "Admin@123", AuthenticationError), # 边界值50
])
def test_login_boundary_values(username, password, expected_exc):
    """测试边界值"""
    with pytest.raises(expected_exc):
        login(username, password)


# ==================== 类型异常测试 ====================

@pytest.mark.parametrize("username, password", [
    (None, "Admin@123"),
    ("admin", None),
    (123, "Admin@123"),
    ("admin", ["pass"]),
])
def test_login_type_errors(username, password):
    """测试非字符串输入触发 TypeError"""
    with pytest.raises(TypeError):
        login(username, password)


# ==================== 特殊字符测试 ====================

@pytest.mark.parametrize("username, password", [
    ("admin@#$", "Admin@123"),
    ("admin", "密码含中文"),
    ("admin", "!@#$%^&*()_+-=[]{}|;:,.<>?"),
])
def test_login_special_chars(username, password):
    """测试特殊字符/Unicode（应该正常抛出认证失败而非崩溃）"""
    with pytest.raises(AuthenticationError):
        login(username, password)