$(function(){

	var camposAValidar = false;
	var dadosFormulario;

	function getCampos() {
		// Faz o serialize e separa em um array a cada '&'
		dadosFormulario = $('#formulario').serialize().split('&');
	}

	function setCampos() {
		//Itera sobre o array, separa em outro array no '=', faz o decode dos caracteres especiais e seta nos campos certos
		for(var i = 0; i<dadosFormulario.length;i++){

			var campo = dadosFormulario[i].split('=')[0];
			var valor  = dadosFormulario[i].split('=')[1];

			//O serialize troca espaço por +, / por %2F e @ por %40. Essas duas linhas trocam pelos caracteres necessários
			valor = valor.replace(/\+/g, " ");
			valor = valor.replace(/\%2F/g, "/");
			valor = valor.replace(/\%40/g, "@");

			$('#'+campo+'-result').text(decodeURI(valor));
		}

		$('#sigla-result').prepend(' (').append( ') - ' );
		$('#sigla-unidade-result').prepend(' (').append( ') - ' );
		$('#endereco-result').append(', ');
		$('#endereco-unidade-result').append(', ');
		$('#cidade-result').append(' - ');
		$('#estado-result').append('. ');
		$('#estado-unidade-result').append('. ');
		$('#rg-result').append(' ');

		//Coloca a data atual
		var dataAtual = new Date()
		var mes = dataAtual.getMonth() + 1;
		var dia = dataAtual.getDate();
		var ano = dataAtual.getFullYear();
		var data = dia + "/" + mes + "/" + ano;
		$('#data-result').text(data);

		//Pega o valor do campo cidade e coloca pra impressão
		var local = $('#cidade').val();
		$('#local-result').text(local);

		//Seta o titulo do formulário Usuario / Novo Chefe
		if ($('#tipo').length > 0) {
			var tipoUsuario = $( '#tipo option:selected' ).text();

			if (tipoUsuario == 'Usuário') {
				$( '#titulo' ).text( 'Formulário para Cadastro de Usuário' );
			} else {
				$( '#titulo' ).text( 'Formulário para Atualização de Chefe de Inteligência' );
			}
		}
	}

	function testaNulos(){
		// Itera sobre o array, separa em outro array no '=', faz o decode dos caracteres especiais e seta nos campos certos
		for(var i = 0; i<dadosFormulario.length;i++){
			var campo = dadosFormulario[i].split('=')[0];
			var valor  = dadosFormulario[i].split('=')[1];

			valor = valor.replace(/\+/g, " ");
			valor = valor.replace(/\%2F/g, "/");
			valor = valor.replace(/\%40/g, "@");

			if (valor =="" || valor == null) {
				mensagemValidacao(campo, 'Campo obrigatório', true);
				camposAValidar = true;
			} else if (campo.indexOf('email') >= 0) {
				validaEmail(campo, valor);
			} else {
				mensagemValidacao(campo, '', false);
			}
		}
	}

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

	function validaEmail(campo, valor) {

		var 	er = /^[a-zA-Z0-9][a-zA-Z0-9\._-]+@([a-zA-Z0-9\._-]+\.)[a-zA-Z-0-9]{2}/;

		if (!er.exec(valor)) {
			camposAValidar = true;
			mensagemValidacao(campo, 'O formato de e-mail está incorreto ', true);
		} else {
			mensagemValidacao(campo, '', false);
		}
	}

	function validaCamposFormulario(e) {
		e.preventDefault();

		getCampos();

		testaNulos();

		ValidaCPF();

		//Se tiver campos a validar o valor da variavel vai ser TRUE
		if (!camposAValidar) {
			setCampos();

			$('.pagina-formulario').css({ display: 'none' });
			$('.pagina-preview').css({ display: 'block' });

		} else {
			//Se for TRUE, não faz nada e reseta o valor pra pessoa preencher os campos de novo
			camposAValidar = false;
		}
	}

	function voltarParaFormulario(e) {
		e.preventDefault();
		$('.pagina-preview').css({ display: 'none' });
		$('.pagina-formulario').css({ display: 'block' });
	}

	function voltarParaPreview(e) {
		e.preventDefault();
		$('.aceito-termos').css({ display: 'block' });
		$('.pagina-impressao').css({ display: 'none' });
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

	function mensagemValidacao(campo, mensagem, mostra) {
		if (mostra == true) {
			$('#'+campo).addClass('campo-validacao');
			$('#validacao-'+campo).text(mensagem);
		} else {
			$('#'+campo).removeClass('campo-validacao');
			$('#validacao-'+campo).text(mensagem);
		}
	}

	//Colocar o caminho relativo quando passar pro liferay
	function cancelar(){
		window.location.href = "sinesp-seguro";
		return false;
	}

	function imprimir() {
		window.print();

	}

	// jQuery Masked Input
	$('#telefoneFixo-unidade').focusout(function(){
		var phone, element;
		element = $(this);
		element.unmask();
		phone = element.val().replace(/\D/g, '');
		if(phone.length > 10) {
			element.mask("(99) 99999-999?9");
		} else {
			element.mask("(99) 9999-9999?9");
		}
	}).trigger('focusout');

	$('#telefoneCelular-chefe').focusout(function(){
		var phone, element;
		element = $(this);
		element.unmask();
		phone = element.val().replace(/\D/g, '');
		if(phone.length > 10) {
			element.mask("(99) 99999-999?9");
		} else {
			element.mask("(99) 9999-9999?9");
		}
	}).trigger('focusout');

	$('#telefoneAutorizador-chefe').focusout(function(){
		var phone, element;
		element = $(this);
		element.unmask();
		phone = element.val().replace(/\D/g, '');
		if(phone.length > 10) {
			element.mask("(99) 99999-999?9");
		} else {
			element.mask("(99) 9999-9999?9");
		}
	}).trigger('focusout');

	$('#telefoneFixo-chefe').focusout(function(){
		var phone, element;
		element = $(this);
		element.unmask();
		phone = element.val().replace(/\D/g, '');
		if(phone.length > 10) {
			element.mask("(99) 99999-999?9");
		} else {
			element.mask("(99) 9999-9999?9");
		}
	}).trigger('focusout');

	$('#telefoneFixo').focusout(function(){
		var phone, element;
		element = $(this);
		element.unmask();
		phone = element.val().replace(/\D/g, '');
		if(phone.length > 10) {
			element.mask("(99) 99999-999?9");
		} else {
			element.mask("(99) 9999-9999?9");
		}
	}).trigger('focusout');

	$('#telefoneCelular').focusout(function(){
		var phone, element;
		element = $(this);
		element.unmask();
		phone = element.val().replace(/\D/g, '');
		if(phone.length > 10) {
			element.mask("(99) 99999-999?9");
		} else {
			element.mask("(99) 9999-9999?9");
		}
	}).trigger('focusout');

	//Todos
	$('#cpf').mask("999.999.999-99");
	$('#nascimento').mask("99/99/9999");

	// Unidade
	$('#telefoneFixo-unidade').mask("(99) 99999-9999");
	$('#cep-unidade').mask("99.999-999");

	// Chefe
	$('#telefoneCelular-chefe').mask("(99) 99999-9999");
	$('#telefoneAutorizador-chefe').mask("(99) 99999-9999");
	$('#telefoneFixo-chefe').mask("(99) 99999-9999");
	$('#nascimento-chefe').mask("99/99/9999");

	//Usuario
	$('#telefoneFixo').mask("(99) 99999-9999");
	$('#telefoneCelular').mask("(99) 99999-9999");
	$('#cep').mask("99.999-999");

	$('#botao-avancar').click(validaCamposFormulario);

	$('#botao-aceito').click(aceitoTermosDeUso);

	$('#botao-voltar-formulario').click(voltarParaFormulario);

	$('#botao-imprimir').click(imprimir);

	$('#botao-voltar-preview').click(voltarParaPreview);

	$('#botao-cancelar').click(cancelar);
	$('#botao-cancelar-preview').click(cancelar);
	$('#botao-cancelar-imprimir').click(cancelar);

})