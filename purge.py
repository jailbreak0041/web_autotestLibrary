from connservice import ParamikoConn

class Purge:
    def purge(self, ip, url):
        cmd = "curl -v  -X PURGE \"" + url + "\" -x 127.0.0.1:51899"
        #print cmd
        ParamikoConn().ssh_conn(ip, cmd)

    def purge(self, ip, url):
        cmd = "curl -v  -X DIR_PURGE \"" + url + "\" -x 127.0.0.1:51899"
        #print cmd
        ParamikoConn().ssh_conn(ip, cmd)

if __name__=='__main__':
     c=Purge()
     c.purge("59.49.85.167","")