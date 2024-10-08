from __future__ import absolute_import

from ciarlare import testing
from ciarlare.utils import richgetter


class TestRichGetter(testing.TestCase):
    def test_resolves_objects(self):
        obj = Namespace(key=Namespace(value='value'))

        result = richgetter(obj, 'key.value')

        self.assertEqual(result, 'value')

    def test_resolves_mappings(self):
        obj = dict(key=dict(value='value'))

        result = richgetter(obj, 'key.value')

        self.assertEqual(result, 'value')

    def test_resolves_sequences(self):
        obj = [['value']]

        result = richgetter(obj, '0.0')

        self.assertEqual(result, 'value')

    def test_resolves_mixed_containers(self):
        obj = Namespace(key=dict(values=['value']))

        result = richgetter(obj, 'key.values.0')

        self.assertEqual(result, 'value')


class Namespace(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
