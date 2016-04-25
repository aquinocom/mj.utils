$(document).ready( function() {

//valida o CPF digitado
	function ValidaCPF(){

		var cpf = $( "#cpf" ).val();
		exp = /\.|\-/g
		cpf = cpf.toString().replace( exp, "" );
		var digitoDigitado = eval(cpf.charAt(9)+cpf.charAt(10));
		var soma1=0, soma2=0;
		var vlr =11;

		for(i=0;i<9;i++){
			soma1+=eval(cpf.charAt(i)*(vlr-1));
			soma2+=eval(cpf.charAt(i)*vlr);
			vlr--;
		}

		soma1 = (((soma1*10)%11)==10 ? 0:((soma1*10)%11));
		soma2=(((soma2+(2*soma1))*10)%11);

		var digitoGerado=(soma1*10)+soma2;

		if(digitoGerado!=digitoDigitado){
			mensagemValidacao('cpf', 'O CPF não é válido!', true)
			camposAValidar = true;
		} else {
			mensagemValidacao('cpf', '', false)
		}
	}

	function mensagemValidacao(campo, mensagem, mostra) {
		if (mostra == true) {
			$('#'+campo).addClass('campo-validacao');
			$('#validacao-'+campo).text(mensagem);
		} else {
			$('#'+campo).removeClass('campo-validacao');
			$('#validacao-'+campo).text(mensagem);
		}
	}

	function aceitoTermosDeUso(){
		if ($('#aceitoTermosUso').is(":checked")){
			mensagemValidacao('aceitoTermos', '', false);
			$('.aceito-termos').css({ display: 'none' });
			$('.pagina-impressao').css({ display: 'block' });
		} else {
			mensagemValidacao('aceitoTermos', 'Aceite os Termos de Uso para prosseguir', true);
		}
	}

	function cancelar(){
		window.location.href = "sinesp-seguro";
		return false;
	}

	function imprimir() {
		window.print();

	}

$('#cpf').mask("999.999.999-99");
$('#data-de-nascimento').mask("99/99/9999");
$('#telefone-fixo').mask("(99) 99999-9999");
$('#telefone-celular').mask("(99) 99999-9999");
$('#cep').mask("99.999-999");


$('#telefoneFixo-unidade').mask("(99) 99999-9999");
$('#cep-unidade').mask("99.999-999");

$('#telefoneCelular-chefe').mask("(99) 99999-9999");
$('#telefoneAutorizador-chefe').mask("(99) 99999-9999");
$('#telefoneFixo-chefe').mask("(99) 99999-9999");
$('#nascimento-chefe').mask("99/99/9999");

ValidaCPF();

$('#botao-aceito').click(aceitoTermosDeUso);

$('#botao-imprimir').click(imprimir);

$('#botao-cancelar').click(cancelar);
$('#botao-cancelar-preview').click(cancelar);
$('#botao-cancelar-imprimir').click(cancelar);



});
