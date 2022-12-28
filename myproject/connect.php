<?php
$servername='127.0.0.1';
$username='root';
$password='';
$dbname='cloud';
$conn=new mysqli($servername,$username,$password);
$conn->set_charset('utf8');
if($conn->connect_error){
    die("error");
}
echo "true";
?>