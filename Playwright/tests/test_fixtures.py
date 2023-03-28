import pytest
def test_status_code(get_req: int):
   assert get_req == 200