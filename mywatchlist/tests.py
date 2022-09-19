from django.test import TestCase, Client

# Create your tests here.

class AppTest(TestCase):
    def test_HTML(self):
        response = Client().post('/mywatchlist/html')
        self.assertEqual(response.status_code,200)
    
    def test_XML(self):
        response = Client().get('/mywatchlist/xml')
        self.assertEqual(response.status_code,200)

    def test_JSON(self):
        response = Client().get('/mywatchlist/json')
        self.assertEqual(response.status_code,200)
