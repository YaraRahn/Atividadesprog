$(function () {

    $(document).on("click", "#btCarregar", function () {

        $.ajax({
            url: 'http://localhost:5000/listar_pessoas',
            method: 'get',
            dataType: 'json',
            success: carregarPessoas,
            error: function () {
                alert("erro ao carregar a lista suspensa, " +
                    "verifique o backend e o console de mensagens do navegador");
            }
        });

        function carregarPessoas(retorno) {
            if (retorno.resultado == 'ok') {
                // percorrer as pessoas ("of" percorre como objetos)
                for (var p of retorno.detalhes) {
                    // adicionar pessoa na lista
                    $("#listasuspensa").append(
                        //$('<option></option').attr('value', p.id).text(p.nome)
                        '<option value =' + p.id + '>' + p.nome + ' - ' + p.email +'</option>'
                    );
                }
            } else {
                alert("erro enviado pelo backend: " + retorno.detalhes);
            }
        }
    });

    $(document).on("click", "#btSelecionado", function () {
        // obter id da opção selecionada
        valor_id = $("#listasuspensa").find(":selected").val();
        // obter descrição da opção selecionada
        valor = $("#listasuspensa").find(":selected").text();
        alert("valor=" + valor + ", id=" + valor_id);
    });
});