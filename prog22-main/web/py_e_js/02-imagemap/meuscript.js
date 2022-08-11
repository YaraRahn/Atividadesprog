$(function () {

    $(document).on("click", "#area_xicara", function () {
        alert("Você clicou na xícara :-) ");
    });

    $(document).on("click", "#destaque_computador", function () {        
        $.ajax({
            url:'http://localhost:5000/listar_pessoas',
            method: 'get',
            dataType: 'json',
            success: carregarPessoas,
            error: function(){ 
                alert("erro, verifique o backend e o console de mensagens do navegador");
            }
        });
        function carregarPessoas(retorno) {
            if (retorno.resultado == 'ok') {
                // percorrer as pessoas ("of" percorre como objetos)
                ret = "Nomes das pessoas que compraram um computador: <br>";
                for (var p of retorno.detalhes) { 
                    ret += p.nome + "<br>";
                }
                $("#nomes_pessoas").append(ret);
            } else {
                alert("erro enviado pelo backend: "+retorno.detalhes);
            }
        }
    });

    $(document).on("click", "#area_celular", function () {
        alert("Este é o telefone do suporte: 47-92332-1232");
    });
    
});