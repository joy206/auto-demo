import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"

@pytest.fixture(scope="session")
def session():
    sess = requests.Session()
    sess.headers.update({"Accept": "application/json"})
    return sess

class TestPetReadOnly:
    """petstore只读接口测试"""

    @pytest.mark.parametrize("pet_id",[1,2,3])
    def test_get_pet_ok(self, pet_id, session):
        """查询相应ID对应的数据存在（非空）"""
        r = session.get(f"{BASE_URL}/pet/{pet_id}")
        assert r.status_code == 200
        assert r.json()['name']

    def test_get_pet_not_found(self, session):
        """查询不存在宠物"""
        r = session.get(f"{BASE_URL}/pet/999999999")
        assert r.status_code == 404

    def test_find_pets_by_status_available(self, session):
        """查 available 宠物，接口必须返回 200 且列表里全是 available 状态的宠物"""
        r = session.get(f"{BASE_URL}/pet/findByStatus", params={"status":"available"})
        assert r.status_code == 200
        assert len(r.json()) > 0
        assert all(p["status"] == "available" for p in r.json())

    def test_find_pets_by_status_sold(self, session):
        """根据status查询sold列表"""
        r = session.get(f"{BASE_URL}/pet/findByStatus", params={"status": "sold"})
        assert r.status_code == 200
        assert len(r.json()) >= 0

