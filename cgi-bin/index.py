#! /usr/bin/env python
# -*- coding: utf-8 -*-
import functions

html = '''
<!DOCTYPE html>
<html lang="cn">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SWEB管理面板 - 首页</title>

<!-- Bootstrap -->
<link rel="stylesheet" href="//cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.css">

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
        <li class="active"><a href="index.py">服务器信息<span class="sr-only">(current)</span></a></li>
        <li><a href="setpage.py">服务设置</a></li>
        <li><a href="log.py">运行日志</a></li>
        <li role="separator" class="divider"></li>
            <li><a href="server.py?action=stop">停止SSR服务器</a> </li>
            <li><a href="server.py?action=start">启动SSR服务器</a> </li>
            <li><a href="server.py?action=restart">重启SSR服务器</a> </li>
              </ul>
            </li>
            <li><a href="v2ray.py">V2ray</a></li>
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

<div class="container-fluid">
 <div class="span12">
    <div class="alert alert-block" style="padding: 8px 35px 8px 14px; background-color: rgb(252, 248, 227); border: 1px solid rgb(251, 238, 213); ">
<h4 style="color: rgb(193, 174, 90);"><strong>服务器状态：</strong>%s</h4>

        </div>
  </div>
  <div class="row-fluid">
<div class="span12">
	  <div class="alert alert-success col-md-offset-0 col-md-6" style="padding: 8px 35px 8px 14px; background-color: rgb(223, 240, 216); border: 1px solid rgb(214, 233, 198); color: rgb(70, 136, 71);"> 
       <strong>服务器IP:</strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s<br>
        <strong>端口:</strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s<br>
		<strong>连接密码:</strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s<br>
       <strong>加密方式:</strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s<br>
        <strong>协议:</strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s<br>
       <strong>混淆:</strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;%s<br>
       <strong>单线程限速:</strong>&nbsp;%sKB/S<br>
       <strong>端口总限速:</strong>&nbsp;%sKB/S
      </div>
      
      <div class="alert alert-info col-md-offset-0 col-md-6" style="padding: 8px 35px 8px 14px; background-color: rgb(217, 237, 247); border: 1px solid rgb(188, 232, 241); color: rgb(58, 135, 173);"> <strong>提示：</strong><br>
		  <li>协议与混淆不支持兼容模式，请严格按照网页上的配置来填写！</li>
        <li>如需使用原版Shadowsocks程序连接，<br>&nbsp;&nbsp;&nbsp;请将协议设置为<strong>origin</strong>,混淆设置为<strong>plain</strong>。</li>
        <li>单线程限速只每一个建立的链接进行限速，值为<strong> 0 </strong>时表示不限速</li>
        <li>端口总限速为对整个端口的传输进行限速，值为<strong> 0 </strong>时表示不限速</li>
        <li>限速不一定准确，会在速度限值左右波动。</li>
        <li>最后一条实在想不出来了。。</li>
      </div>
      
	</div>
		<div class="panel panel-default">
		<div class="panel-heading">
			<h4 class="panel-title">
				<a data-toggle="collapse" data-parent="#accordion" 
				   href="#collapseThree">
					点击我查看二维码 / 配置文件
				</a>
			</h4>
		</div>
		<div id="collapseThree" class="panel-collapse collapse">
			<div class="panel-body">
				SSR链接:<br>
				<textarea class="input-xlarge trololo" id="textarea" rows="3" style="background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); padding: 4px; border: 1px solid rgb(204, 204, 204); font-size: 16px; margin: 0px; width: 100%%; height: 50%%;">%s</textarea><br>
				
				二维码：<img src="http://qr.liantu.com/api.php?&w=150?&text=%s"/>
			</div>
		</div>
	</div>
</div>
</div>



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

print html % (functions.serverstatus(),functions.getip(),functions.server_port,functions.password,functions.method,functions.protocol,functions.obfs,functions.speed_limit_per_con,functions.speed_limit_per_user,functions.getssrlink(),functions.getssrlink())

