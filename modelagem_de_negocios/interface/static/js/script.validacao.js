$(document).ready(function(){
				$("#cadastrocliente").validate({
					rules:{
						senha: {
							required: true,
							minlength: 8
						}
					},
					submitHandler: function(form){
						alert("Concluído")
					}
				})
			})