#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import urllib2
import commands
import base64
#打开并且读取JSON配置文件
jsonfile = file("/etc/shadowsocks.json")

myjson = json.load(jsonfile)

#将配置文件内容整理导入
server_port=str(myjson[u"server_port"])
password=str(myjson[u"password"])
method=str(myjson[u"method"])
protocol=str(myjson[u"protocol"])
protocol_param=str(myjson[u"protocol_param"])
obfs=str(myjson[u"obfs"])
obfs_param=str(myjson[u"obfs_param"])
speed_limit_per_user=str(myjson[u"speed_limit_per_user"])
speed_limit_per_con=str(myjson[u"speed_limit_per_con"])

def openiptables(port):
    #拼接字符串，生成iptables命令
    cmd1="iptables -I INPUT -m state --state NEW -m tcp -p tcp --dport " + str(port) + " -j ACCEPT"
    cmd2="iptables -I INPUT -m state --state NEW -m udp -p udp --dport " + str(port) + " -j ACCEPT"
    #执行iptables命令，开启防火墙
    os.system(cmd1)
    os.system(cmd2)

def set(setport,setpassword,setmethod,setprotocol,setprotocol_param,setobfs,setobfs_param,setspeed_limit_per_user,setspeed_limit_per_con):
    myjson[u"server_port"]=int(setport)
    myjson[u"password"]=str(setpassword)
    myjson[u"method"]=str(setmethod)
    myjson[u"protocol"]=str(setprotocol)
    myjson[u"protocol_param"]=str(setprotocol_param)
    myjson[u"obfs"]=str(setobfs)
    myjson[u"obfs_param"]=str(setobfs_param)
    myjson[u"speed_limit_per_user"]=int(setspeed_limit_per_user)
    myjson[u"speed_limit_per_con"]=int(setspeed_limit_per_con)
    myjsondump=json.dumps(myjson,indent=1)
    openjsonfile=file("/etc/shadowsocks.json","w+")
    openjsonfile.writelines(myjsondump)
    openjsonfile.close()
    openiptables(setport)
    restartss()


def stopss():
    os.system('/etc/init.d/shadowsocks stop >/dev/null 2>&1')

def startss():
    os.system('/etc/init.d/shadowsocks start >/dev/null 2>&1')
    openiptables(server_port)

def restartss():
    os.system('/etc/init.d/shadowsocks restart >/dev/null 2>&1')
    openiptables(server_port)

def getip():
    myip = urllib2.urlopen('http://members.3322.org/dyndns/getip').read()
    myip = myip.strip()
    return str(myip)

def serverstatus():
    cmd='''ps -ef | grep -v grep | grep -i "/usr/local/shadowsocks/server.py" | awk '{print $2}' '''
    (status, PID) = commands.getstatusoutput(cmd)
    if PID!="":
        return "运行中"
    else:
        return "已停止"

def printlogs():
    logfile = open('/var/log/shadowsocksr.log', 'r')
    log=logfile.read()
    logfile.close()
    return log

def getssrlink():
    link = "%s:%s:%s:%s:%s:%s/?obfsparam=%s&protoparam=%s" % (getip(),server_port,protocol,method,obfs,base64.b64encode(password),base64.b64encode(obfs_param),base64.b64encode(protocol_param))
    ssrlink="ssr://%s" % (base64.b64encode(link))
    return ssrlink


def clearhistory():
    os.system('rm -rf /var/log/shadowsocksr.log')
    os.system('touch /var/log/shadowsocksr.log')

