import urllib3

def test_home():
    http = urllib3.PoolManager()
    r = http.request('GET', "http://35.197.235.163:5000/")
    assert r.status == 200

def test_about():
    http = urllib3.PoolManager()
    r = http.request('GET', "http://35.197.235.163:5000/about")
    assert r.status == 200

def test_history():
    http = urllib3.PoolManager()
    r = http.request('GET', "http://35.197.235.163:5000/history")
    assert r.status == 200

def test_submit():
    http = urllib3.PoolManager()
    r = http.request('GET', "http://35.197.235.163:5000/submit")
    assert r.status == 200

def test_browse():
    http = urllib3.PoolManager()
    r = http.request('GET', "http://35.197.235.163:5000/browse")
    assert r.status == 200

def test_mvp():
    http = urllib3.PoolManager()
    r = http.request('GET', "http://35.197.235.163:5000/mvp")
    assert r.status == 200

def test_negative():
    http = urllib3.PoolManager()
    r = http.request('GET', "http://35.197.235.163:5000/negative")
    assert r.status == 404