#! /usr/bin/env python
# -*- coding: utf-8 -*-
import v2rayfunctions
import cgi

header='''
<!DOCTYPE html>
<html lang="cn">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SWEB管理面板 - 首页</title>

<!-- Bootstrap -->
<link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.css">

<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
<!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
</head>
<body>
<nav class="navbar navbar-default">
  <div class="container-fluid"> 
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false"> <span class="sr-only">Toggle navigation</span> <span class="icon-bar"></span> <span class="icon-bar"></span> <span class="icon-bar"></span> </button>
      <a class="navbar-brand" href="#">SWEB管理面板</a></div>
    
    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li>
              <a href="#"  data-toggle="dropdown" >SSR<b class="caret"></b></a>
              <ul class="dropdown-menu">
        <li><a href="index.py">服务器信息<span class="sr-only">(current)</span></a></li>
        <li><a href="setpage.py">服务设置</a></li>
        <li><a href="log.py">运行日志</a></li>
        <li role="separator" class="divider"></li>
            <li><a href="server.py?action=stop">停止SSR服务器</a> </li>
            <li><a href="server.py?action=start">启动SSR服务器</a> </li>
            <li><a href="server.py?action=restart">重启SSR服务器</a> </li>
              </ul>
            </li>
            <li class="active"><a href="v2ray.py">V2ray<span class="sr-only">(current)</span></a></li>
        <li><a href="app.py">软件下载</a></li>
      </ul>
<ul class="nav navbar-nav navbar-right">
        <li> </li>
        <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false" aria-haspopup="true">菜单 <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="https://github.com/FunctionClub/SWEB">关于</a> </li>
            <li><a href="support.py">支持赞助</a> </li>
          </ul>
        </li>
      </ul>
    </div>
    <!-- /.navbar-collapse --> 
  </div>
  <!-- /.container-fluid --> 
</nav>

<!-- HEADER --><!-- / HEADER --> 
'''

footer='''
<!--  FOOTER --> 
<footer class="text-center">
  <div class="container">
    <div class="row">
      <div class="col-xs-12">
        <p>Copyright © FunctionClub. All rights reserved.</p>
      </div>
    </div>
  </div>
</footer>
<!-- / FOOTER --> 
<!-- jQuery (necessary for Bootstrap's JavaScript plugins) --> 
<script src="//cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script> 
<!-- Include all compiled plugins (below), or include individual files as needed --> 
<script src="//cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.js"></script>
</body>
</html>
'''

form = cgi.FieldStorage()
if form.has_key('action'):
    action = form['action'].value
else:
    exit()

if action=="start":
    v2rayfunctions.startv2()
    html="""
        <div class="span12">
    <div class="alert alert-block col-md-12" style="padding: 8px 35px 8px 14px; background-color: rgb(252, 248, 227); border: 1px solid rgb(251, 238, 213); ">
<h4 style="color: rgb(193, 174, 90);"><strong>V2ray服务器已启动！</strong></h4><br>
        </div>
  </div>
  <div class="row-fluid"> </div>
</div>
    """
if action=="stop":
    v2rayfunctions.stopv2()
    html='''
        <div class="span12">
    <div class="alert alert-block col-md-12" style="padding: 8px 35px 8px 14px; background-color: rgb(252, 248, 227); border: 1px solid rgb(251, 238, 213); ">
<h4 style="color: rgb(193, 174, 90);"><strong>V2ray服务器已停止！</strong></h4><br>
        </div>
  </div>
  <div class="row-fluid"> </div>
</div>
    '''
if action=="restart":
    v2rayfunctions.restartv2()
    html='''
        <div class="span12">
    <div class="alert alert-block col-md-12" style="padding: 8px 35px 8px 14px; background-color: rgb(252, 248, 227); border: 1px solid rgb(251, 238, 213); ">
<h4 style="color: rgb(193, 174, 90);"><strong>V2ray服务器已重启！</strong></h4><br>
        </div>
  </div>
  <div class="row-fluid"> </div>
</div>
    '''

print header
print html
print footer
