from lacinizatar import lacin


def test_j_l():
    assert lacin('Лье') == 'Lje'
    assert lacin('лье') == 'lje'
    assert lacin('льюць') == 'ljuć'
    assert lacin('лямант') == 'lamant'
    assert lacin('лекар') == 'lekar'
    assert lacin('лёс') == 'los'
    assert lacin('людзі') == 'ludzi'


def test_j_u():
    assert lacin('я ўяўляю') == 'ja ŭjaŭlaju'

def test_j_soft():
    assert lacin('зьеў') == 'źjeŭ'
    assert lacin('пасьянс') == 'paśjans'
