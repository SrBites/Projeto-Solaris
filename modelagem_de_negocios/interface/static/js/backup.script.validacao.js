jQuery.validator.addMethod("validaSenha", function(value, element){
    const num = /[0-9]/;
    const let = /a-zA-Z/+;

    if (num.test(value) || let.test(value)){
        return true
    } else{
        return false
    }
}, "A senha deve conter ao menos uma letra e um número")

$(document).ready(function(){
    $("#cadastrocliente").validate{
        rules: {
            senha: {
                validaSenha: true
            }
        }
    }
    $("#cadastroempresa").validate{
        rules: {
            senha: {
                validaSenha: true
            }
        }
    }
})