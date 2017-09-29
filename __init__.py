from connservice import ParamikoConn
from curltest import CurlTest
from getlog import GetLog
#__version__ = VERSION



class web_autotestLibrary(ParamikoConn,CurlTest,GetLog):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'