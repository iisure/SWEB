#! /usr/bin/env python
# -*- coding: utf-8 -*-

html='''
<!DOCTYPE html>
<html lang="cn">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SWEB控制面板 - 支持赞助</title>

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
        <li><a href="app.py">软件下载</a></li>
      </ul>
<ul class="nav navbar-nav navbar-right">
        <li> </li>
        <li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-expanded="false" aria-haspopup="true">菜单 <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="https://github.com/FunctionClub/SWEB">关于</a> </li>
            <li class="active"><a href="support.py">支持赞助<span class="sr-only">(current)</span></a> </li>
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
	<div class="alert alert-info" style="padding: 8px 35px 8px 14px; background-color: rgb(217, 237, 247); border: 1px solid rgb(188, 232, 241); color: rgb(58, 135, 173);"> <strong>感谢：</strong><br> 非常感谢你能点开这个页面。这里的每一分钱的赞助都将是激励我继续前进的动力。<br><br>
    <strong>支持以下方式：</strong><br><br>
     <div class="panel panel-default">
		<div class="panel-heading" >
			<h4 class="panel-title">
				<a data-toggle="collapse" data-parent="#accordion" 
				   href="#collapseThree">
					支付宝 / 微信
				</a>
			</h4>
		</div>
		<div id="collapseThree" class="panel-collapse collapse">
			<div class="panel-body" align="center">
				<img src="https://cdn.ylws.me/support.png"/>
			</div>
		</div>
</div>


<div class="panel panel-default">
		<div class="panel-heading" >
			<h4 class="panel-title">
				<a data-toggle="collapse" data-parent="#accordion" 
				   href="#collapseFour">
					AFF赞助
				</a>
			</h4>
		</div>
		<div id="collapseFour" class="panel-collapse collapse">
			<div class="panel-body" align="center">
			<strong>欢迎走我的AFF购买以下产品，允许我拿一些回扣。嘻嘻嘻</strong><br><br>
				<a href="https://www.tizipu.net/aff.php?aff=46"><img src="https://cdn.ylws.me/tizipu.png"></a><br><br>
				<a href="http://www.vultr.com/?ref=6985881"><img src="https://cdn.ylws.me/vultr.png"></a>
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

print html
