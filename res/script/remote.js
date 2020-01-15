//when pressed the conditions become true
volumeUpCond = false
volumeDownCond = false
muteCond = false


$("button#volumeUp").on("vmousedown",function(){
	volumeUpCond = true

	$(this).attr("data-pressCond",1)
})
$("button#volumeUp").on("vmouseup",function(){
	volumeUpCond = false

	$(this).attr("data-pressCond",0)
})

$("button#volumeDown").on("vmousedown",function(){
	volumeDownCond = true

	$(this).attr("data-pressCond",1)
})
$("button#volumeDown").on("vmouseup",function(){
	volumeDownCond = false

	$(this).attr("data-pressCond",0)
})

$("button#volumeMute").click(function(){
	volume = 0
	buttonPress("toggleMute")
	if($(this).attr("data-pressCond") == 0){
		$(this).attr("data-pressCond",1)
	}else{
		$(this).attr("data-pressCond",0)
	}
})

$("button#playPause").click(function(){
	buttonPress("togglePlayPause")
})

$("button#skipBack").click(function(){
	buttonPress("skipPrevious")
})

$("button#skipNext").click(function(){
	buttonPress("skipNext")
})

function buttonPress(actionInput){
	$.ajax({
		type:"POST",
		data:{
			action:actionInput
		}
	})
}

function update(){
	if($("button#volumeUp").attr("data-pressCond") == 1){
		buttonPress("increaseVolume")
		$("button#volumeMute").attr("data-pressCond",0)
	}else if($("button#volumeDown").attr("data-pressCond") == 1){
		buttonPress("decreaseVolume")
		$("button#volumeMute").attr("data-pressCond",0)
	}

	$("button[data-pressCond=1]").addClass("pressed")
	$("button[data-pressCond=0]").removeClass("pressed")

	setTimeout(update,100)
	
}

function updateResponse(result){

	setTimeout(update,100)
}

update()
