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
<title>SWEB管理面板 - 软件下载</title>

<!-- Bootstrap -->
<link rel="stylesheet" href="//cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.css">

<!-- FontAwesome -->
<link rel="stylesheet" href="/css/font-awesome.css">

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
            <li><a href="v2ray.py">V2ray</a></li>
        <li class="active"><a href="app.py">软件下载<span class="sr-only">(current)</span></a></li>
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


<div id="download" class="container">

     <div class="col-md-4">
     	<h3><i class="fa fa-windows fa-3x"></i> &nbsp; Windows</h3><p><strong>图形客户端</strong></p><ul><li>ShadowsocksR: <a href="https://github.com/shadowsocksr/shadowsocksr-csharp/releases">点击下载</a></li></ul>
     </div>
      <div class="col-md-4">
     	<div class="one-third column"><h3><i class="fa fa-apple fa-3x"></i> &nbsp; Mac OS X</h3><p><strong>图形客户端</strong></p><ul><li>ShadowsocksX-NG: <a href="https://github.com/shadowsocksr/ShadowsocksX-NG/releases">点击下载</a></li></ul><p><strong>命令行工具</strong></p><ul><li><code>pip install shadowsocks</code></li><li><code>brew install shadowsocks-libev</code></li><li><code>cpan Net::Shadowsocks</code></li></ul></div>
     </div>
      <div class="col-md-4">
     	<div class="one-third column"><h3><i class="fa fa-linux fa-3x"></i> &nbsp; Linux</h3><p><strong>图形客户端</strong></p><ul><li>Shadowsocks-Qt5: <a href="https://github.com/shadowsocks/shadowsocks-qt5/wiki/Installation">GitHub</a></li></ul><p><strong>命令行工具</strong></p><ul><li><code>pip install shadowsocks</code></li><li><code>apt-get install shadowsocks-libev</code></li><li><code>cpan Net::Shadowsocks</code></li></ul></div>
     </div><br>

     <p class="sixteen columns"></p>

              <div class="col-md-4">
     <div class="one-third column last"><h3><i class="fa fa-android fa-3x"></i> &nbsp; Android</h3><ul><li>Shadowsocksr-Android:<ul><li><a href="https://github.com/shadowsocksr/shadowsocksr-android/releases">点击下载</a> </li></ul></li></ul></div>
     </div>
              <div class="col-md-4">
     	<div class="one-third column last"><h3><i class="fa fa-apple fa-3x"></i> &nbsp; iOS</h3><ul><li>ShadowRocket:<ul><li><a href="https://itunes.apple.com/cn/app/shadowrocket/id932747118">App Store</a></li></ul></li><li>越狱版:<ul><li><a href="http://apt.thebigboss.org/onepackage.php?bundleid=com.linusyang.shadowsocks">Big Boss</a></li></ul></li></ul></div>
     </div>
              <div class="col-md-4">
     	<div class="one-third column last"><h3><i class="fa fa-rss fa-flip-horizontal fa-3x"></i> &nbsp; OpenWRT</h3><ul><li>Shadowsocks-libev</li><ul><li><code>opkg install shadowsocks-libev</code></li></ul><li>Shadowsocks-libev-polarssl</li><ul><li><code>opkg install shadowsocks-libev-polarssl</code></li></ul></ul></div>
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

print html
