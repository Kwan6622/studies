from um import count  

def test_single_um():
    assert count("um") == 1
    assert count("UM") == 1
    assert count("Um") == 1

def test_multiple_um():
    assert count("um um um") == 3
    assert count("UM um Um") == 3
    assert count("um, um. um!") == 3

def test_um_with_text():
    assert count("Quang said um") == 1
    assert count("um Quang um") == 2
    assert count("um, Quang replied, um.") == 2
    assert count("I am thinking... um") == 1

def test_no_um():
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("UMM no thanks") == 0
    assert count("hmm...") == 0

def test_edge_cases():
    assert count("") == 0
    assert count(" ") == 0
    assert count("um?") == 1
    assert count("um!") == 1
    assert count("um.") == 1
