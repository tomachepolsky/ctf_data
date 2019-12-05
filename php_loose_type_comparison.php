<?php
include('flag.php');
echo "    <h1>cant see anything hmm</h1>";
echo "<!-- ?source usually helps !-->";
if(isset($_GET['source'])){
    highlight_file(__FILE__);
}
if (!isset($_GET["md5"]))
{
    die();
}

if ($_GET["md5"] == hash("md5", $_GET["md5"]))
{echo $flag[0];}
else
{echo "bad";}
if (!isset($_GET["md4"]))
{
    die();
}
if ($_GET["md4"] == hash("md4", $_GET["md4"]))
{echo $flag[1];}
else
{echo "bad";}


?>
