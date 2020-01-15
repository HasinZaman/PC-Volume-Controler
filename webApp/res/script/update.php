<?php 
//session_start();

function createRemote(){
	$conn = new mysqli(DB_SERVER, DB_NAME, DB_PASSWORD, DB_DATABASE);

	$command = $conn->prepare("INSERT INTO `remoteTable`(`remoteId`, `actionId`, `volume`, `action`, `lastUpdate`, `password`) VALUES (?,?,0,'000',?,?)");

	$remoteId = uniqid();

	$actionId = uniqid();

	$date = new DateTime();
	$timeStamp = $date->getTimestamp();
	$password = PasswordStorage::create_hash($_POST["password"]);

	$command->bind_param("ssss",$remoteId,$actionId,$timeStamp,$password);

	$_SESSION["remoteId"] = $remoteId;
	$_SESSION["password"] = $password;

	echo $remoteId;

	$conn->close();
}

function update(){
	$conn = new mysqli(DB_SERVER, DB_NAME, DB_PASSWORD, DB_DATABASE);

	$command = $conn->prepare("UPDATE remoteTable SET actionId=?, volume=?, action=? lastUpdate=? WHERE remoteId=? AND password=?");

	$actionId = uniqid();

	$date = new DateTime();
	$timeStamp = $date->getTimestamp();

	$command->bind_param("sissss",$actionId,$_POST["volume"],$_POST["action"],$timeStamp,$_SESSION["remoteId"],$_SESSION["pasword"]);

	echo $command->execute();

	$conn->close();
}


function close(){
	$conn = new mysqli(DB_SERVER, DB_NAME, DB_PASSWORD, DB_DATABASE);

	$command = $conn->prepare("DELETE FROM `remoteTable` WHERE remoteId=? AND password=?");

	$command->bind_param("SS",$_SESSION["remoteId"],$_SESSION["pasword"]);

	echo $command->execute();

	$conn->close();

	$_SESSION["remoteId"]="";
	$_SESSION["pasword"]="";
}
?>