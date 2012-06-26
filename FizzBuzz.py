"""
Q1. Why is the report method untestable ? [2 pts]
    report method untestable calls to external dependencies i.e.  file operations 



Q2. How will you change the api of the report method to make it more testable ? [2 pts]
     def report(self, numbers, proxyfilehandler): or 
     def report(self, numbers, fileOpener=open):
     and in the function replace open with fileOpener. 
     If no fileOpener is specified. we will call the default Open method 

"""
class FizzBuzz(object):
     def report(self, numbers, fileOpener=open):

        report_file = fileOpener('c:/temp/fizzbuzz_report.txt', 'w')

        for number in numbers:
            msg = str(number) + " "
            fizzbuzz_found = False
            if number % 3 == 0:
                msg += "fizz "
                fizzbuzz_found = True
            if number % 5 == 0:
                msg += "buzz "
                fizzbuzz_found = True

            if fizzbuzz_found:
                report_file.write(msg + "\n")

        report_file.close()

if "__main__" == __name__:
    fb = FizzBuzz()
    fb.report(range(100))

            
