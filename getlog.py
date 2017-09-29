from connservice import ParamikoConn
import time

class GetLog:
    def get_last_line(self,ip,service,filename):
        if service == 'ATS':
            if filename == 'access.log':
                cmd = 'awk \'NF{a=$0}END{print a}\' /usr/local/squid/var/logs/access.log'
                log = ParamikoConn().ssh_conn(ip, cmd)
                return log
        elif service == 'NGINX':
            if filename == 'access.log':
                cmd = 'awk \'NF{a=$0}END{print a}\' /usr/local/nginx/log/access.log'
                log = ParamikoConn().ssh_conn(ip, cmd)
                return log

    def hsa_get_last_line(self,ip,service,filename,ua):
        if service == 'ATS':
            if filename == 'access.log':
                cmd = 'awk \'{if($17~"' + str(ua) + '") print}\'  /home/aca/dca/var/log/trafficserver/dca.log'
                #print cmd
                time.sleep(10)
                #print ip
                a = str(ip)
                log = ParamikoConn().ssh_conn(a, cmd)
                f = open('log.txt','w')
                f.write(log)
                f.close()
                f1 = open('log.txt', 'r')
                lastline = f1.readlines()[-1]
                #print lastline
                f1.close()
                return lastline.split()
        elif service == 'NGINX':
            if filename == 'access.log':
                cmd = 'awk \'NF{a=$0}END{print a}\' /usr/local/nginx/log/access.log'
                log = ParamikoConn().ssh_conn(ip, cmd)
                return log

    def get_hittype(self,ip,service,filename,reshittype='TCP_MEM_HIT'):
        hittype = GetLog().get_last_line(ip,service,filename)
        if hittype[5] == 'TCP_MEM_HIT':
            pass
        else:
            raise Exception("hit type is " + hittype[5])

    def hsa_get_hittype(self,ip,service,filename,ua,typelist=['TCP_MEM_HIT','TCP_HIT']):
        hittype = GetLog().hsa_get_last_line(ip,service,filename,ua)
        #print hittype
        if hittype[5] in typelist:
            pass
        else:
            raise Exception("hit type is " + hittype[5])

if __name__=='__main__':
    c=GetLog()
    c.hsa_get_hittype("59.49.85.167","ATS","access.log","-")
