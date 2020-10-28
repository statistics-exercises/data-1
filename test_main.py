import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_xvalues(self) :
       fighand=plt.gca()
       figdat = fighand.get_lines()[0].get_xydata()
       this_x, this_y = zip(*figdat)
       for i in range( len(this_x) ) :
           self.assertTrue( np.abs(i+1 - this_x[i])<1e-7, "One or more of the x-coordinates in your graph are not correct." )
  
    def test_yvalues(self):
       fighand=plt.gca()
       figdat = fighand.get_lines()[0].get_xydata()
       this_x, this_y = zip(*figdat)
       myy = np.loadtxt("data.dat")
       for i in range( len(myy) ) :
           self.assertTrue( np.abs(myy[i] - this_y[i])<1e-7, "One or more of the y-coordinates in your graph are not correct." )
