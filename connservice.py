import paramiko

class ParamikoConn:
    def ssh_conn(self, ip, cmd):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, 55667, "root", "10GsKPNS@FNOp20e612", timeout=20)
            stdin, stdout, stderr = ssh.exec_command(cmd)
            stdin.write("Y")
            #logstr = stdout.read().split()
            logstr = stdout.read()
            # logstr = stdout.read()
            return logstr
            # print a
            # print a.split()ip
            # for x  in  stdout.readlines():
            #     print x.split()
            # print '%stOKn' % (ip)
            ssh.close()
        except:
            print '%stErrorn' % (ip)


if __name__=='__main__':
     c=ParamikoConn()
     c.ssh_conn("59.49.85.167","ifconfig")