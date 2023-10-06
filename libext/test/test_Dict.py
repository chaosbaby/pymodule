from libext.Dict import Dict

def test_dict_sign_obj_get():
    d = Dict()
    d['name'] = "chaos"
    assert d.name == "chaos"


    

def test_get_sub_dic_value():
    my_dict = {
        'name': 'chaos',
        'address': {
            'country': 'Country A',
            'city': 'City A',
            'codes': [1, 2, 3]
        },
    }
    d = Dict(my_dict)
    assert d.address.city == 'City A'
    assert d.address.codes == [1, 2, 3]
    assert d.address.country == 'Country A'
    assert d['address']['city'] == 'City A'
    assert d['address']['codes'] == [1, 2, 3]
    assert d['address']['country'] == 'Country A'

def test_set_sub_value_without_pre_set():
    d = Dict()
    d.address.city = 'City A'
    d.address.codes = [1, 2, 3]
    d.address.country = 'Country A'
    assert d['address']['city'] == 'City A'
    assert d['address']['codes'] == [1, 2, 3]
    assert d['address']['country'] == 'Country A'

def test_to_dic():
    d = Dict()
    d.address.city = 'City A'
    d.address.codes = [1, 2, 3]
    d.address.country = 'Country A'
    d_dic = d.to_dict()
    assert type(d_dic) == dict
    assert d_dic['address']['city'] == 'City A'
    assert d_dic['address']['codes'] == [1, 2, 3]
    assert d_dic['address']['country'] == 'Country A'

    
import pytest
if __name__ == "__main__":
    pytest.main()
    
