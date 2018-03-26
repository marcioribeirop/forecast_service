import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from forecast_service.web.views.forecast_views import forecast_view
        request = testing.DummyRequest()
        info = forecast_view(request)
        self.assertEqual(info['project'], 'Forecast Service')


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from forecast_service import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'Pyramid' in res.body)
