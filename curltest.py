import subprocess
import shlex
import connservice

class CurlTest:
    def curl_normal(self, url):
        com = "curl \"" + url + "\" -v -o /dev/null"
        #print com
        args = shlex.split(com)
        # print args
        val = subprocess.Popen(args, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        response = val.stdout.read()
        return response


    def curl_ua(self, url,ua):
        com = "curl -H \"User-Agent:" + str(ua) +  "\" " + url + " -v -o /dev/null"
        #print com
        args = shlex.split(com)
        # print args
        val = subprocess.Popen(args, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        response = val.stdout.read()
        return response


    def curl_httpcode(self, url, spe_code='200'):
        com = "curl -sL -w \"%{http_code}\" \"" + url + "\" -o /dev/null"
        #print com
        args = shlex.split(com)
        # print args
        val = subprocess.Popen(args, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        res_code = val.stdout.read()
        if (res_code == spe_code):
            pass
        else:
            raise Exception("code exception! code is " + res_code)

    def curl_histype(self,url,hittype):
        response = CurlTest().curl_normal(url)
        for l in response.split("\n"):
            if 'HitType' in l:
                hitstatus = l.split(":")[1].strip()
        if hitstatus == hittype:
            pass
        else:
            raise Exception(hitstatus)



if __name__=='__main__':
     c=CurlTest()
     c.curl_ua("http://www.dnion.com",10)



