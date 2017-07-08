#!/usr/bin/env python
#coding: utf-8
import sys, os
import hackhttp
import time
import json
import paramiko
import sinamail
import poplib

def send_mail(m):
    email = ""
    password = ""
    pop3_server = "pop.sina.cn"
    # 连接到POP3服务器:
    server = poplib.POP3(pop3_server)
    # 可以打开或关闭调试信息:
    # server.set_debuglevel(1)
    # 可选:打印POP3服务器的欢迎文字:
    print(server.getwelcome())
    # 身份认证:
    server.user(email)
    server.pass_(password)
    '''
    # stat()返回邮件数量和占用空间:
    print('Messages: %s. Size: %s' % server.stat())
    # list()返回所有邮件的编号:
    resp, mails, octets = server.list()
    # 可以查看返回的列表类似['1 82923', '2 2184', ...]
    print(mails)
    # 获取最新一封邮件, 注意索引号从1开始:
    index = len(mails)
    print index


    resp, lines, octets = server.retr(index)
    # lines存储了邮件的原始文本的每一行,
    # 可以获得整个邮件的原始文本:
    msg_content = '\r\n'.join(lines)
    # 稍后解析出邮件:
    msg = Parser().parsestr(msg_content)
    print_info(msg)
    # 可以根据邮件索引号直接从服务器删除邮件:
    # server.dele(index)
    # 关闭连接:
    server.quit()
    '''


    #SendEmail("123654dagao@sina.cn","1@sztb.gov.cn","","test","just a test");
    #SendEmail("123654dagao@sina.cn","756810697111111111111111111111@qq.com","","test","jus

    sinamail.SendEmail("","","zmap","test",m)

def connect():
    try:
        ssh = paramiko.SSHClient(ip,username,passwd)
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username = uaername, password = passwd, timeout = 300)
        cmd = 'sudo git clone https://github.com/comahax/webzmap.git'
        ssh.exec_command(cmd)
        cmd = 'sudo sh ~/webzmap/init.sh'
        ssh.exec_command(cmd)
        send_mail('http://'+ip+':8000')

    except Exception,e:
        print e


#定义raw
raw1 = '''
POST /v1/single_runtime/nodes HTTP/1.1
Host: api.daocloud.io
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0
Accept: application/json, text/plain, */*
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate, br
UserNameSpace:
Authorization: IjQ0ZTNiNTIwLTA1YmItNDdlNi1iNGNmLWIwZWU0NmJmNjhhOCI.DD84Hg.5qlg3TvF8jDYoiR_VSWePFOcDe4
Content-Type: application/json;charset=utf-8
Referer: https://dashboard.daocloud.io/nodes/new?cluster_token=a576dc35c5e718f8ec722d2f737f3ee3619f4ba2&cluster_id=b08281a6-2acc-4c36-8a33-527863ee093c
Content-Length: 135
Origin: https://dashboard.daocloud.io
Connection: close

{"stream_room":"e8b260d7.1499320551.0929c168b6e52f5c5c55eff1f51efd34a8fcf567","node_cluster_id":"b08281a6-2acc-4c36-8a33-527863ee093c"}
'''

def createM():
    hh = hackhttp.hackhttp()

    code, head, html, redirect, log = hh.http('http://api.daocloud.io/v1/single_runtime/nodes', raw=raw)
    print html
    if "sandbox_password" in html:
        r_j = json.loads(html)
        ip = r_j['node']['sandbox_ip_address']
        username = 'ubuntu'
        passwd =  r_j['node']['sandbox_password']


def print_ts(message):
    print "[%s] %s" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), message)



'''将当前进程fork为一个守护进程
   注意：如果你的守护进程是由inetd启动的，不要这样做！inetd完成了
   所有需要做的事情，包括重定向标准文件描述符，需要做的事情只有chdir()和umask()了
'''

def daemonize (stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
     #重定向标准文件描述符（默认情况下定向到/dev/null）
    try:
        pid = os.fork()
          #父进程(会话组头领进程)退出，这意味着一个非会话组头领进程永远不能重新获得控制终端。
        if pid > 0:
            sys.exit(0)   #父进程退出
    except OSError, e:
        sys.stderr.write ("fork #1 failed: (%d) %s\n" % (e.errno, e.strerror) )
        sys.exit(1)

     #从母体环境脱离
    os.chdir("/")  #chdir确认进程不保持任何目录于使用状态，否则不能umount一个文件系统。也可以改变到对于守护程序运行重要的文件所在目录
    os.umask(0)    #调用umask(0)以便拥有对于写的任何东西的完全控制，因为有时不知道继承了什么样的umask。
    os.setsid()    #setsid调用成功后，进程成为新的会话组长和新的进程组长，并与原来的登录会话和进程组脱离。

     #执行第二次fork
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)   #第二个父进程退出
    except OSError, e:
        sys.stderr.write ("fork #2 failed: (%d) %s\n" % (e.errno, e.strerror) )
        sys.exit(1)

     #进程已经是守护进程了，重定向标准文件描述符

    for f in sys.stdout, sys.stderr: f.flush()
    si = open(stdin, 'r')
    so = open(stdout, 'a+')
    se = open(stderr, 'a+', 0)
    os.dup2(si.fileno(), sys.stdin.fileno())    #dup2函数原子化关闭和复制文件描述符
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

#示例函数：每秒打印一个数字和时间戳
def main():
    import time
    sys.stdout.write('Daemon started with pid %d\n' % os.getpid())
    sys.stdout.write('Daemon stdout output\n')
    sys.stderr.write('Daemon stderr output\n')
    c = 0
    '''
    while True:
        sys.stdout.write('%d: %s\n' %(c, time.ctime()))
        sys.stdout.flush()
        c = c+1
        time.sleep(1)
    '''
    while True:
        try:
            # sleep for the remaining seconds of interval
            time_remaining = interval - time.time() % interval
            print_ts("Sleeping until %s (%s seconds)..." % ((time.ctime(time.time() + time_remaining)), time_remaining))
            time.sleep(time_remaining)
            print_ts("Starting command.")
            # execute the command
            #status = os.system(command)
            createM()
            print_ts("-" * 100)
            #print_ts("Command status = %s." % status)
        except Exception, e:
            print e




if __name__ == "__main__":
    send_mail("a")

    daemonize('/dev/null','/tmp/daemon_stdout.log','/tmp/daemon_error.log')
    main()

