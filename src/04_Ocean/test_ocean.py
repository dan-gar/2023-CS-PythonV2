from ocean import Ocean


def test_ocean_init():
    a=Ocean([[2]])
    assert type(a)==Ocean
    assert a.state==[[2]]


def test_ocean_repr():
    a=Ocean([[2]])
    assert eval(repr(a))


def test_ocean_step():
    a=Ocean([[0,2,0,1,3],
             [0,2,0,3,3],
             [0,2,2,2,1],
             [2,1,2,0,3],
             [3,3,1,3,3]])
    
    b=Ocean([[0,0,0,1,3],
             [2,2,0,3,3],
             [2,0,0,2,1],
             [0,1,2,2,3],
             [0,0,1,3,3]])
    
    assert a.gen_next_quantum().state==b.state
