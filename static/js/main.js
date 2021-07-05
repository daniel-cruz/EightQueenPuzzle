var start=null;
var cron;

$( document ).ready(function() {
    calculateN();
	iterateN();
});

function iterateN(){
	$("#iterate").click(
		function(event){
			event.preventDefault();
			start=new Date();
			if($("#queensNumber").val()>8){
				$("#statusBar").addClass("visually-hidden");
				$("#display-wrapper").addClass("visually-hidden");
				$("#store-wrapper").addClass("visually-hidden");
				$.ajax({
					url: "/iterate?n=" + $("#queensNumber").val(),
					beforeSend: function(){
						counter=0;
						$("#calculate").attr('disabled','disabled');
						$("#iterate").attr('disabled','disabled');
						cron = setInterval(timer,1)
					},
					success: function(result){
						clearInterval(cron);
						if(result.code){
							$("#statusBar").removeClass("visually-hidden").removeClass("alert-success").addClass("alert-danger").html('<p class="float-start">Se encontraron '+result.message+' soluciones</p><p class="text-end float-end">Tiempo: '+displayTime(new Date() - start)+'</p>');
						}else{
							$("#statusBar").removeClass("visually-hidden").removeClass("alert-danger").addClass("alert-success").html('<p class="float-start">'+result.message+'</p><p class="text-end float-end">Tiempo: '+displayTime(new Date() - start)+'</p>');
							$("#display-wrapper").removeClass("visually-hidden");
							$("#store-wrapper").removeClass("visually-hidden");
						}
					
						$("#calculate").removeAttr("disabled").val("Calculate");
						$("#iterate").removeAttr("disabled").val("Iterate");
					}
				});
			}
			else{
				$("#statusBar").removeClass("visually-hidden").removeClass("alert-success").addClass("alert-danger").html('<p class="float-start">Error: el input debe ser mayor a 8 para iterar</p><p class="text-end float-end">Tiempo: '+displayTime(new Date() - start)+'</p>');
			}
		}
	);
}

function calculateN(){
	$("#calculate").click(
		function(event){
			event.preventDefault();
			$("#statusBar").addClass("visually-hidden");
			$("#display-wrapper").addClass("visually-hidden");
			$("#store-wrapper").addClass("visually-hidden");
			$.ajax({
				url: "/calculate?n=" + $("#queensNumber").val(),
				beforeSend: function(){
					counter=0;
					$("#calculate").attr('disabled','disabled');
					$("#iterate").attr('disabled','disabled');
					start=new Date();
					cron = setInterval(timer,1)
				},
				success: function(result){
					clearInterval(cron);
					if(result.code){
						$("#statusBar").removeClass("visually-hidden").removeClass("alert-success").addClass("alert-danger").html('<p class="float-start">Se encontraron '+result.message+' soluciones</p><p class="text-end float-end">Tiempo: '+displayTime(new Date() - start)+'</p>');
					}else{
						$("#statusBar").removeClass("visually-hidden").removeClass("alert-danger").addClass("alert-success").html('<p class="float-start">'+result.message+'</p><p class="text-end float-end">Tiempo: '+displayTime(new Date() - start)+'</p>');
						$("#display-wrapper").removeClass("visually-hidden");
						$("#store-wrapper").removeClass("visually-hidden");
					}
				
					$("#calculate").removeAttr("disabled").val("Calculate");
					$("#iterate").removeAttr("disabled").val("Iterate");
				}
			});
		}
	);
}
function timer(){
    $("#calculate").val(displayTime(new Date() - start));
}
function pad(n, z) {
    z = z || 2;
    return ('00' + n).slice(-z);
  }
function displayTime(time){
	var ms = time % 1000;
	time = (time - ms) / 1000;
	var secs = time % 60;
	time = (time - secs) / 60;
	var mins = time % 60;
	var hrs = (time - mins) / 60;
	return pad(hrs) + ':' + pad(mins) + ':' + pad(secs) + '.' + pad(ms, 3);
}