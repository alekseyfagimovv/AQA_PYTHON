import pytest


@pytest.fixture
def program(request):
    return request.param

@pytest.mark.parametrize("program, result", [
    ("anydesk", "anydesk start"),
    ("virus",   "virus start"),
], indirect=["program"])
def test_get_start_indirect(program, result):
    assert get_start(program) == result

def get_start(program: str):
    return f'{program} start'

@pytest.mark.smoke
@pytest.mark.parametrize("program, result", [
    pytest.param("anydesk", 'anydesk start', id='anydesk start'),
    pytest.param("virus", 'virus start', id='virus start'),
    pytest.param("browser", 'browser start', id='browser start'),
])
def test_get_start(program, result):
    assert get_start(program) == result
    

@pytest.mark.skip(reason="not released")
def test_program_name_start_qe():
    assert get_start('program_name_qe') == False

@pytest.mark.xfail(reason="BAG-019", strict=True)
def test_program_name_start():
    assert get_start('program_name') == False