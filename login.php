<?php

session_start();
include("includes/config.php");

if($_SERVER["REQUEST_METHOD"] == "POST")
{
	$myusername = addslashes($_POST['username']);
	$mypassword = md5(addslashes($_POST['password']));
	
	$sql = "SELECT userid FROM tbl_users WHERE username='$myusername' and password='$mypassword'";
	$result = mysql_query($sql);
	$count = mysql_num_rows($result);
	if ($sql->connect_error) {
	    die("Connection failed: " . $sql->connect_error);
	}
	if($count == 1){
		$_SESSION['login_admin']=$myusername;
		header("location: http://127.0.0.1:8080/Cem/admin/index.php");
	}
}
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    

    <title>Signin Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="Sylesheets/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="style/signin.css" rel="stylesheet">


  </head>

  <body>

    <div class="container">

      <form class="form-signin" method="post">
        <h2 class="form-signin-heading">Login</h2>
        <label for="inputEmail" class="sr-only">Email address</label>
        <input name="username" type="email" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>
        <label for="inputPassword" class="sr-only">Password</label>
        <input name="password" type="password" id="inputPassword" class="form-control" placeholder="Password" required>
        <div class="checkbox">
          <label>
            <input type="checkbox" value="remember-me"> Remember me
          </label>
        </div>
        <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
      </form>

    </div> <!-- /container -->


	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
	<script src="Scripts/bootstrap.min.js"></script>
  </body>
</html>

	