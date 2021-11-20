import unittest
from datetime import datetime

#Unit Test in Python
#Kenna Bogue

#You should write unit tests for the five inputs from the
#stock visualizer challenge that enforce the following constraints.

#symbol: capitalized, 1-7 alpha characters
#chart type: 1 numeric character, 1 or 2
#time series: 1 numeric character, 1 - 4
#start date: date type YYYY-MM-DD
#end date: date type YYYY-MM-DD

class SimpleTest(unittest.TestCase):
    def testSymbol(self):
          stockSymbol = input('\nEnter stock symbol: ')  
          self.assertEqual(stockSymbol.upper(), 'TSLA')
    def testChartType(self):
        chartType = int(input('\nEnter the chart type you want(1, 2): '))
        self.assertIn(chartType,[1,2])
    def testTimeSeries(self):
        timeSeries = int(input('\nEnter  time series option (1, 2, 3, 4): '))
        self.assertIn(timeSeries,[1,2,3,4])
    def testStartDate(self):
        startDate = input('\nEnter the start date (format: YYYY-MM-DD): ')
        self.assertTrue(datetime.strptime(startDate, "%Y-%m-%d"),"correct format")
    def testEndDate(self):
        endDate = input('\nEnter the end date (format: YYYY-MM-DD): ')
        self.assertTrue(datetime.strptime(endDate, "%Y-%m-%d"),"correct format")
 

if __name__ == '__main__':
    unittest.main()
