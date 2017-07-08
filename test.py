#coding:utf-8
import sinamail
import poplib
if __name__ == '__main__':
    email = "123654dagao@sina.cn"
    password = "4399opklnm"
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
    #SendEmail("123654dagao@sina.cn","756810697111111111111111111111@qq.com","","test","just a test");

    sinamail.SendEmail("123654dagao@sina.cn","756810697@qq.com","","test","just a test")