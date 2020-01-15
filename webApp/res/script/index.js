
$("#startSession").click(function(){
	password = prompt("set Password")

	$.ajax({
		type: "POST",
		url: "res/script/post.php",
		data:{
			method: "createRemote",
			password: password
		}
	}).done(function(remoteId){
		console.log(remoteId)
		window.location.replace("remote.php?id="+remoteId);
	})
})