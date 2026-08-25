import requests
import pytest
from selenium import webdriver
'''@pytest.fixture
def create_user_via_api():
    """通过接口创建测试用户，测试完再删掉"""
    resp = requests.post("https://api.example.com/users", json={
        "name": "test_user", "email": "test@example.com"
    })
    user_id = resp.json()["id"]
    yield user_id
    # 清理：删除测试用户
    requests.delete(f"https://api.example.com/users/{user_id}")

def test_ui_with_api_data(create_user_via_api, driver):
    """用 API 造的数据，去 UI 上验证"""
    driver.get(f"https://example.com/users/{create_user_via_api}")
    assert "test_user" in driver.page_source'''

from faker import Faker

fake = Faker("zh_CN")  # 中文数据

print(fake.name())        # 张伟
print(fake.email())       # xiuying@example.com
print(fake.phone_number()) # 13904567891
print(fake.address())     # 河北省石家庄市朝阳区中山路p座 375号
print(fake.text(max_nb_chars=50))  # 随机一段中文

# 生成 5 个用户数据
users = [{"name": fake.name(), "email": fake.email()} for _ in range(5)]