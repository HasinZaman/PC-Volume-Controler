<?php

session_start();

include "server.php";
include "update.php";
require_once('PasswordStorage.php');


echo $_POST["method"]();


?>