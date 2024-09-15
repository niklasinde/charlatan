import unittest

import ciarlare

fixtures_manager = ciarlare.FixturesManager()
fixtures_manager.load("./docs/examples/simple_fixtures.yaml")


class TestToaster(unittest.TestCase, ciarlare.FixturesManagerMixin):

    def setUp(self):
        # Attach the fixtures manager to the instance
        self.fixtures_manager = fixtures_manager
        # Cleanup the cache
        self.init_fixtures()

    def test_example(self):
        """Verify that we can get fixtures."""
        toaster = self.install_fixture("toaster")
        self.assertEqual(toaster.color, "red")
        self.assertEqual(toaster.slots, 5)
        self.assertEqual(toaster.content, ['Toast 1', 'Toast 2'])
