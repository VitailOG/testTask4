from ..services import get_unique_domains


def test_unique_domains():
    test_data = [
        'https://regex101.com/',
        'https://regex101.com/dsadasd',
        'https://stackoverflow.com/questions/19282580/redis-return-all-values-stored-in-a-database',
        'https://fastapi.tiangolo.com/deployment/docker/'
    ]
    res = get_unique_domains(test_data)
    assert len(res) == 3
    assert isinstance(res, set)
