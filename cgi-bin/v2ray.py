#! /usr/bin/env python
# -*- coding: utf-8 -*-
import v2rayfunctions

html = '''
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

<div class="container-fluid">
  <div class="span12">
   <div class="col-md-4"></div>
 <div class="col-md-4">
    <div class="panel-group" id="accordion">
	<div class="panel panel-primary">
		<div class="panel-heading">
			<h4 class="panel-title">
				<a data-toggle="collapse" data-parent="#accordion" 
				   href="#collapseOne">
					服务管理
				</a>
			</h4>
		</div>
		<div id="collapseOne" class="panel-collapse collapse in">
			<div class="panel-body">
               <div class="col-md-1"></div>

				<button type="button" class="btn btn-success " onClick="window.open('v2rayserver.py?action=start')">启动V2ray</button>
        <button type="button" class="btn btn-danger" onClick="window.open('v2rayserver.py?action=stop')">停止V2ray</button>
        <button type="button" class="btn btn-warning" onClick="window.open('v2rayserver.py?action=restart')">重启V2ray</button>

           <div class="col-md-1"></div>
			</div>
		</div>
	</div>
</div>
</div>
   <div class="col-md-4"></div>

  </div>
  </div>
  
  <div class="container-fluid">

<div class="span12">

<div class="col-md-4"></div>
   <div class="col-md-4">
<div class="panel panel-primary">
	<div class="panel-heading">
		<h3 class="panel-title">服务配置</h3>
	</div>
          <form class="form-horizontal" role="form" action="setv2ray.py">
	<div class="panel-body">

      

	<div class="form-group">
		<label for="firstname" class="col-sm-2 control-label">主端口号</label>
		<div class="col-sm-8">
			<input type="text" class="form-control" name="mainport" 
				   placeholder="请输入主端口号" value="%s">
</div>	<div class="col-sm-1">

<button type="button" class="btn btn-default" title="主端口号"
                        data-container="body" data-toggle="popover" data-placement="right"
                        data-content="服务器上开放的端口，用于连接你的电脑和服务器。">?</button>
</div>
</div>
  	<div class="form-group">
		<label for="firstname" class="col-sm-2 control-label">传输协议</label>
		<div class="col-sm-8">
					<select class="form-control" name="transport">
			<option value="%s">%s</option>
			<option vaule="1">TCP</option>
			<option value="2">HTTP伪装</option>
			<option value="3">mKCP</option>
		</select>
		</div>
<div class="col-sm-1">

<button type="button" class="btn btn-default" title="传输协议"
                        data-container="body" data-toggle="popover" data-placement="right"
                        data-content="服务器与客户端电脑之间的通讯协议，TCP为默认协议，HTTP伪装是伪装成访问正常网站，mKCP是修改版的KCP协议">?</button>
</div>

	</div>

<div class="form-group">
		<label for="firstname" class="col-sm-2 control-label">Mux.Cool</label>
		<div class="col-sm-8">
					<select class="form-control" name="mux">
        <option value="%s">%s</option>
			<option value="1">启用</option>
			<option value="2">禁用</option>

		</select>
		</div>
<div class="col-sm-1">

<button type="button" class="btn btn-default" title="Mux多路复用"
                        data-container="body" data-toggle="popover" data-placement="right"
                        data-content="试验阶段，开启后可以流畅观看直播等网站">?</button>
</div>

	</div>

    	<div class="form-group">
		<label for="firstname" class="col-sm-2 control-label">代理模式</label>
		<div class="col-sm-8">
					<select class="form-control" name="type">
        <option>%s</option>
			<option>socks</option>
			<option>http</option>

		</select>
		</div>
<div class="col-sm-1">

<button type="button" class="btn btn-default" title="代理模式"
                        data-container="body" data-toggle="popover" data-placement="right"
                        data-content="客户端上的代理协议选自，可选择 Socks代理 或者 http代理">?</button>
</div>

	</div>
  <div class="form-group">
	<label for="firstname" class="col-sm-2 control-label">代理端口</label>
	
	<div class="col-sm-8">
			<input type="text" class="form-control" name="localport" width="80%%" 
				   placeholder="请输入本地代理端口" value="%s"> 
	</div>	
<div class="col-sm-1"><button type="button" width="20%%" class="btn btn-default" title="代理端口"
                        data-container="body" data-toggle="popover" data-placement="right"
                        data-content="本地客户端的代理端口，默认设置为1080">?</button>
</div>

	</div>


<div class="col-md-7"></div>
<button type="submit" class="btn btn-success">保存按钮</button>
<div class="col-md-1"></div>

	</div>

  </form>
</div>
</div>
   <div class="col-md-4"></div>

</div>
</div>

<div class="container-fluid">
  <div class="span12">
   <div class="col-md-4"></div>
 <div class="col-md-4">
    <div class="panel-group" id="accordion">
	<div class="panel panel-primary">
		<div class="panel-heading">
			<h4 class="panel-title">
				<a data-toggle="collapse" data-parent="#accordion" 
				   href="#collapseOne">
					客户端下载
				</a>
			</h4>
		</div>
		<div id="collapseOne" class="panel-collapse collapse in">
			<div class="panel-body">


				<div align="center">
					<button type="button" class="btn btn-info " onClick="window.open('/v2ray-client/client.zip')">
						Windows客户端+配置文件
						</button>
					<br><br>
					<button type="button" class="btn btn-success" onclick="window.open('/config.json')">
						仅下载 config.json
						</button>
				</div>


			</div>
		</div>
	</div>
</div>
</div>
   <div class="col-md-4"></div>

  </div>
  </div>



 <div class="container-fluid">
<div class="span12">
<div class="col-md-4"></div>
 <div class="col-md-4">
    <div class="panel-group" id="accordion">
	<div class="panel panel-primary">
		<div class="panel-heading">
			<h4 class="panel-title">
				<a data-toggle="collapse" data-parent="#accordion" 
				   href="#collapseOne">
					运行日志
				</a>
			</h4>
		</div>
		<div id="collapseOne" class="panel-collapse collapse in">
			<div class="panel-body">
				<div class="form-group">
		<textarea class="form-control" rows="4">%s</textarea>
	</div>
			</div>
		</div>
	</div>
</div>
</div>
   <div class="col-md-4"></div>
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
<script src="http://cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script> 
<!-- Include all compiled plugins (below), or include individual files as needed --> 
<script src="http://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.js"></script>
<script>
$(function () { 
	$("[data-toggle='popover']").popover();
});
	</script>

</body>
</html>
'''

print html %(v2rayfunctions.mainport,v2rayfunctions.transport,v2rayfunctions.printtransport(),v2rayfunctions.mux,v2rayfunctions.printmux(),v2rayfunctions.printtype(),v2rayfunctions.localport,v2rayfunctions.printlogs())
