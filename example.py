from iogui import ioform
import json


@ioform(form_name='Test form 1')
def test_func(value):
    result = json.loads(value)
    result.append('a')
    return json.dumps(result)


test_func()
