import sys
from datetime import datetime, timezone

import requests


def test_index():
    print(requests.get("http://127.0.0.1:8000/").json())


def test_post():
    # Example measurement data
    data = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "bus_id": "lv3",
        "p_kw": 5.0,
        "q_kvar": 1.2,
        "v_pu": 1.01,
    }
    print(requests.post("http://127.0.0.1:8000/meas", json=data).json())
    data = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "bus_id": "lv4",
        "p_kw": 4.0,
        "q_kvar": -1.2,
        "v_pu": 1.02,
    }
    print(requests.post("http://127.0.0.1:8000/meas", json=data).json())


def test_get():
    print(requests.get("http://127.0.0.1:8000/meas?limit=50").json())


def test_delete_one():
    print(requests.delete("http://127.0.0.1:8000/meas/4").json())


def test_delete():
    print(requests.delete("http://127.0.0.1:8000/meas", json=[5, 6, 7, 8, 9]).json())


def test_update():
    data = {"bus_id": "lv3", "p_kw": 4.0, "q_kvar": 1.5, "v_pu": 1.03}
    print(requests.patch("http://127.0.0.1:8000/meas/3", json=data).json())


# Map names to functions
funcs = {
    "index": test_index,
    "post": test_post,
    "get": test_get,
    "del_one": test_delete_one,
    "del": test_delete,
    "update": test_update,
}

if __name__ == "__main__":
    funcs[sys.argv[1]]()
