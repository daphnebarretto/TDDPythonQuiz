import unittest
import pymock
import FizzBuzz
"""
Q3. What will be printed when we execute 'python FizzBuzzStubbed.py' ? [3 pts]
setUpClass FizzBuzzStubbed
setup
test_report
teardown
setup
test_report
teardown
tearDownClass

Q4. Implement MyStub class so that you can send it as a fake object to the
    report method of FizzBuzz object from a test case. [3 pts]

"""
class MyStub(object):
 
    def __init__(self):
        self.values = []
		
	def write(self, value):
        self.values.append(value)
	    
    def close(self):
        self.closed = True

    def gen_open_stub(self):
        def open(fpath, mode):
            return self
        return open    

    
class TestFizzBuzzStubbed(unittest.TestCase):
        
    @classmethod
    def setUpClass(cls):
        print "setUpClass FizzBuzzStubbed"
        
    def setUp(self):
        super(TestFizzBuzzStubbed, self).setUp()
        self.fb = FizzBuzz.FizzBuzz()
        print "setup"

    @classmethod
    def tearDownClass(cls):
        print "tearDownClass"
        
    def tearDown(self):
        super(TestFizzBuzzStubbed, self).tearDown()
        self.fb = None
        print "teardown"

    def test_report(self):
        print "test_report"
        mystub = MyStub()
      	numbers =[1,2,3,4]
      	fileOpener = mystub.gen_open_stub()		
      	report(numbers, fileOpener)
      	self.assertEqual(values[0], '3 fizz \n')	

    def test_report_for_empty_list(self):
        print "test_report"
        mystub = MyStub()
        numbers =[]
        fileOpener = mystub.gen_open_stub()		
        report(numbers, fileOpener)
        # assert that values is empty. \donno how to do it in python :)

if __name__ == "__main__":
    unittest.main()
