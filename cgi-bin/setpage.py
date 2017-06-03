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
<title>SWEB管理面板 - 服务设置</title>

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
        <li class="active"><a href="setpage.py">服务设置<span class="sr-only">(current)</span></a></li>
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
      <div class="alert alert-info col-md-offset-0 col-md-12" style="padding: 8px 35px 8px 14px; background-color: rgb(217, 237, 247); border: 1px solid rgb(188, 232, 241); color: rgb(58, 135, 173);"> <strong>提示：</strong><br>
      <li>本面板不支持_compatible兼容设置，请使用SSR客户端连接。</li>
      <li>协议参数和混淆参数默认为空，<strong>请勿乱填。</strong></li>
      <li>限速功能填写 <strong> 0 </strong>表示不限速！</li>
      
      </div>
  </div>
  <div class="row-fluid">
<div class="span12">
  <form action="set.py" method="post">
	  <div class="alert alert-success col-md-offset-0 col-md-12" style="padding: 8px 35px 8px 14px; background-color: rgb(223, 240, 216); border: 1px solid rgb(214, 233, 198); color: rgb(70, 136, 71);"> 

		<div class="col-md-3">
			<strong>端口号:</strong><br><input type="text" class="input-xlarge trololo" name="setport" style="background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); padding: 3px; border: 1px solid rgb(204, 204, 204); font-size: 16px;" data-enpassid="__811" value="%s"><br><br>
			<strong>密码:<br></strong><textarea class="input-xlarge trololo" name="setpassword" rows="3" style="background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); padding: 3px; border: 1px solid rgb(204, 204, 204); font-size: 15px;" data-enpassid="__816">%s</textarea>
			
		</div>
        <div class="col-md-3">
        <strong>加密方式:</strong><br><select name="setmethod" class="trololo" style="background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); padding: 4px; border: 1px solid rgb(204, 204, 204); font-size: 16px;" data-enpassid="__813">
            <option>%s</option>
            <option>aes-256-cfb</option>
            <option>aes-128-cfb</option>
            <option>rc4-md5</option>
            <option>aes-128-ctr</option>
            <option>aes-256-ctr</option>
            <option>chacha20</option>
            <option>chacha20-ietf</option>
            <option>salsa20</option>
          </select><br><br>
			<strong>协议方式:</strong><br><select name="setprotocol" class="trololo" style="background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); padding: 4px; border: 1px solid rgb(204, 204, 204); font-size: 16px;" data-enpassid="__813">
            <option>%s</option>
            <option>origin</option>
            <option>auth_sha1_v4</option>
            <option>rc4-md5</option>
            <option>verify_deflate</option>
            <option>auth_aes128_sha1</option>
            <option>auth_aes128_md5</option>
          </select><br><br>
          <strong>混淆方式:</strong><br><select name="setobfs" class="trololo" style="background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); padding: 4px; border: 1px solid rgb(204, 204, 204); font-size: 16px;" data-enpassid="__813">
			<option>%s</option>
            <option>plain</option>
            <option>http_simple</option>
            <option>http_post</option>
            <option>tls1.2_ticket_auth</option>
          </select>
        </div>
        <div class="col-md-3">
				<strong>协议参数:<br></strong>
      			<textarea class="input-xlarge trololo" name="setprotocol_param" rows="2" style="background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); padding: 3px; border: 1px solid rgb(204, 204, 204); font-size: 15px;" data-enpassid="__816">%s</textarea><br>
       			<strong>混淆参数:<br></strong><textarea class="input-xlarge trololo" name="setobfs_param" rows="2" style="background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); padding: 3px; border: 1px solid rgb(204, 204, 204); font-size: 15px;" data-enpassid="__816">%s</textarea><br>
        </div>
        <div class="col-md-3">
       			<strong>单线程限速:<br></strong><input type="text" class="input-xlarge trololo" name="setspeed_limit_per_con" style="background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); padding: 3px; border: 1px solid rgb(204, 204, 204); font-size: 13px;" data-enpassid="__811" value="%s"><strong> KB/S<br><br></strong> 
       			<strong>总端口限速:<br></strong><input type="text" class="input-xlarge trololo" name="setspeed_limit_per_user" style="background-color: rgb(255, 255, 255); color: rgb(85, 85, 85); padding: 3px; border: 1px solid rgb(204, 204, 204); font-size: 13px;" data-enpassid="__811" value="%s"><strong> KB/S<br></strong> 
       			<br>
       			<button class="btn btn-success" style="color: rgb(255, 255, 255); background-image: -webkit-linear-gradient(top, rgb(98, 196, 98), rgb(81, 163, 81)); background-color: rgb(70, 136, 71);" type="submit"><i class="icon-ok icon-white"></i>提交</button>
       			
        </div>
      </div>
      
</form>
      
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

print html %(functions.server_port,functions.password,functions.method,functions.protocol,functions.obfs,functions.protocol_param,functions.obfs_param,functions.speed_limit_per_con,functions.speed_limit_per_user)
