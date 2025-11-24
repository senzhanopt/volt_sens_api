import requests
import sys
from datetime import datetime, timezone

def test_index():
    print(requests.get("http://127.0.0.1:8000/").json())

def test_post():
    # Example measurement data
    data = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "bus_id": "lv1",
        "p_kw": 5.0,
        "q_kvar": 1.2,
        "v_pu": 1.01
    }
    print(requests.post("http://127.0.0.1:8000/meas", json=data).json())
    data = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "bus_id": "lv2",
        "p_kw": 4.0,
        "q_kvar": -1.2,
        "v_pu": 1.02
    }
    print(requests.post("http://127.0.0.1:8000/meas", json=data).json())

def test_get():
    print(requests.get("http://127.0.0.1:8000/meas?limit=1").json())

# Map names to functions
funcs = {
    "index": test_index,
    "post": test_post,
    "get": test_get
}

if __name__ == "__main__":
    funcs[sys.argv[1]]()