import unittest
from models import sources
Source = sources.Source

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_sources = Source(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs','8.5','129993','Rwa')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,Source)

if __name__ == '__main__':
    unittest.main()