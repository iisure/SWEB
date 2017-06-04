#! /usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import urllib2
import commands


v2rayjson = file("/etc/v2ray/myv2ray.json")
myv2json = json.load(v2rayjson)

mainport=str(myv2json[u"mainport"])
localport=str(myv2json[u"localport"])
transport=str(myv2json[u"transport"])
mux=str(myv2json[u"mux"])

def printtransport():
    returntransport=""
    if myv2json[u"transport"] == "1":
        returntransport="TCP"
    if myv2json[u"transport"] == "2":
        returntransport="HTTP伪装"
    if myv2json[u"transport"] == "3":
        returntransport="mKCP"
    return returntransport

def printmux():
    mux=""
    if myv2json[u"mux"] == "1":
        returnmux = "启用"
    if myv2json[u"mux"] == "2":
        returnmux = "禁用"
    return returnmux

def printtype():
    type=""
    if myv2json[u"type"] == "1":
        type="socks"
    else:
        type="http"
    return type

def openiptables(port):
    #拼接字符串，生成iptables命令
    cmd1="iptables -I INPUT -m state --state NEW -m tcp -p tcp --dport " + str(port) + " -j ACCEPT"
    cmd2="iptables -I INPUT -m state --state NEW -m udp -p udp --dport " + str(port) + " -j ACCEPT"
    #执行iptables命令，开启防火墙
    os.system(cmd1)
    os.system(cmd2)

def getip():
    myip = urllib2.urlopen('http://members.3322.org/dyndns/getip').read()
    myip = myip.strip()
    return str(myip)

def printlogs():
    logfile = open('/var/log/v2ray/access.log', 'r')
    log=logfile.read()
    logfile.close()
    return log

def startv2():
    startcmd="service v2ray start >/dev/null 2>&1"
    os.system(startcmd)
    openiptables(mainport)

def stopv2():
    stopcmd="service v2ray stop >/dev/null 2>&1"
    os.system(stopcmd)

def restartv2():
    restartcmd="service v2ray restart >/dev/null 2>&1"
    os.system(restartcmd)



def genjson(getmainport,gettransport,gettype,getmux,getlocalport):
    uuidcmd="cat /proc/sys/kernel/random/uuid"
    genuuid=commands.getoutput(uuidcmd)

    if gettransport == "1":
        gentransport=""
    if gettransport == "2":
        gentransport='''
        ,
    "streamSettings": {
      "network": "tcp",
      "tcpSettings": {
        "connectionReuse": true,
        "header": {
          "type": "http",
          "request": {
            "version": "1.1",
            "method": "GET",
            "path": ["/"],
            "headers": {
              "Host": ["www.baidu.com", "www.sogou.com/"],
              "User-Agent": [
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36",
                        "Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/53.0.2785.109 Mobile/14A456 Safari/601.1.46"
              ],
              "Accept-Encoding": ["gzip, deflate"],
              "Connection": ["keep-alive"],
              "Pragma": "no-cache"
            }
          },
          "response": {
            "version": "1.1",
            "status": "200",
            "reason": "OK",
            "headers": {
              "Content-Type": ["application/octet-stream", "application/x-msdownload", "text/html", "application/x-shockwave-flash"],
              "Transfer-Encoding": ["chunked"],
              "Connection": ["keep-alive"],
              "Pragma": "no-cache"
            }
          }
        }
      }
    }
        '''
    if gettransport == "3":
        gentransport='''
        ,
   		 		"streamSettings": {
   			 	"network": "kcp"
  				}
        '''

    if getmux == "1":
        genmux='''
        ,
    "mux": {
      "enabled": true
    }
        '''
    else:
        genmux =""
    serverjson = '''
    {"log" : {
    "access": "/var/log/v2ray/access.log",
    "error": "/var/log/v2ray/error.log",
    "loglevel": "warning"
  },
  "inbound": {
    "port": ''' + str(getmainport) + ''',
    "protocol": "vmess",
    "settings": {
        "clients": [
            {
                "id": "''' + str(genuuid) + '''",
                "level": 1,
                "alterId": 100
            }
        ]
    }''' + str(gentransport) +'''
  },
  "outbound": {
    "protocol": "freedom",
    "settings": {}
  },

      

  "outboundDetour": [
    {
      "protocol": "blackhole",
      "settings": {},
      "tag": "blocked"
    }
  ],
  "routing": {
    "strategy": "rules",
    "settings": {
      "rules": [
        {
          "type": "field",
          "ip": [
            "0.0.0.0/8",
            "10.0.0.0/8",
            "100.64.0.0/10",
            "127.0.0.0/8",
            "169.254.0.0/16",
            "172.16.0.0/12",
            "192.0.0.0/24",
            "192.0.2.0/24",
            "192.168.0.0/16",
            "198.18.0.0/15",
            "198.51.100.0/24",
            "203.0.113.0/24",
            "::1/128",
            "fc00::/7",
            "fe80::/10"
          ],
          "outboundTag": "blocked"
        }
      ]
    }
  }
}
    '''
    f = open('/etc/v2ray/config.json', 'w')
    f.write(serverjson)
    f.close()



    clientjson='''
    {
  "log": {
    "loglevel": "info"
  },
  "inbound": {
    "port": '''+ str(getlocalport) +''',
    "listen": "127.0.0.1",
    "protocol": "'''+ str(gettype) +'''",
    "settings": {
      "auth": "noauth",
      "udp": true,
      "ip": "127.0.0.1"
    }
  },
  "outbound": {
    "protocol": "vmess",
    "settings": {
        "vnext": [
            {
                "address": "'''+ str(getip()) +'''",
                "port": '''+ getmainport + ''',
                "users": [
                    {
                        "id": "'''+ str(genuuid) +'''",
                        "alterId": 100
                    }
                ]
            }
        ]
    }''' + str(gentransport) + str(genmux) +'''
    
  },
  "outboundDetour": [
    {
      "protocol": "freedom",
      "settings": {},
      "tag": "direct"
    }
  ],
  "dns": {
    "servers": [
      "8.8.8.8",
      "8.8.4.4",
      "localhost"
    ]
  },
  "routing": {
    "strategy": "rules",
    "settings": {
      "rules": [
        {
          "type": "chinasites",
          "outboundTag": "direct"
        },
        {
          "type": "field",
          "ip": [
            "0.0.0.0/8",
            "10.0.0.0/8",
            "100.64.0.0/10",
            "127.0.0.0/8",
            "169.254.0.0/16",
            "172.16.0.0/12",
            "192.0.0.0/24",
            "192.0.2.0/24",
            "192.168.0.0/16",
            "198.18.0.0/15",
            "198.51.100.0/24",
            "203.0.113.0/24",
            "::1/128",
            "fc00::/7",
            "fe80::/10"
          ],
          "outboundTag": "direct"
        },
        {
          "type": "chinaip",
          "outboundTag": "direct"
        }
      ]
    }
  }
}

    '''
    f = open('/usr/local/SWEB/config.json', 'w')
    f.write(clientjson)
    f.close()

    #SAVE JSON
    myv2json[u"mainport"]=getmainport
    myv2json[u"localport"]=getlocalport
    myv2json[u"transport"]=gettransport
    myv2json[u"mux"]=getmux
    myv2json[u"type"]=gettype
    myv2jsondump = json.dumps(myv2json, indent=1)
    openjsonfile = file("/etc/v2ray/myv2ray.json", "w+")
    openjsonfile.writelines(myv2jsondump)
    openjsonfile.close()
    openiptables(getmainport)
    restartv2()

def genclient():
    cpcmd="rm -rf /usr/local/SWEB/v2ray-client/config.json && cp /usr/local/SWEB/config.json /usr/local/SWEB/v2ray-client/"
    zipcmd="rm -rf /usr/local/SWEB/v2ray-client/client.zip && cd /usr/local/SWEB/ && zip -r /usr/local/SWEB/client.zip v2ray-client/ && mv /usr/local/SWEB/client.zip /usr/local/SWEB/v2ray-client/"
    os.system(cpcmd)
    os.system(zipcmd)


