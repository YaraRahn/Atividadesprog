// qual a função do parâmetro debug=True no comando run? detalhar os erros da página
// é possível fazer o teste da API via linha de comando no terminal do linux? Como? $ curl localhost:5000/retornar_pessoas
// faça o FOR equivalente ao for "inline" que existe no código do backend
//pessoas = db.session.query(Pessoa).all()
//pessoas_em_json = []
//for x in pessoas:
//    pessoas_em_json.append(x.json())
// um desafio consiste em criar o backend e frontend das classes Casa, Quarto e Mobilia

$(function () { // quando o documento estiver pronto/carregado

    // chamada ao backend
    $.ajax({
        url: 'http://localhost:5000/retornar_pessoas',
        method: 'GET',
        dataType: 'json', // os dados são recebidos no formato json
        success: listar, // chama a função listar para processar o resultado
        error: function () {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    

    // função executada quando tudo dá certo
    function listar(casa) {
        // percorrer a lista de casas retornadas; 
        for (var i in casa) { //i vale a posição no vetor
            lin = '<tr>' + // elabora linha com os dados da casa
                '<td>' + casa[i].formato + '</td>' +
                '<td>' + casa[i].quartos + '</td>' +
                '</tr>';
            // adiciona a linha no corpo da tabela
            $('#corpoTabelaCasa').append(lin);
        }
    }
    /*
    // função executada quando tudo dá certo
    function listar(quarto) {
        // percorrer a lista de quartos retornadas; 
        for (var i in quarto) { //i vale a posição no vetor
            lin = '<tr>' + // elabora linha com os dados da quarto
                '<td>' + quarto[i].nome + '</td>' +
                '<td>' + quarto[i].dimensoes + '</td>' +
                '</tr>';
            // adiciona a linha no corpo da tabela
            $('#corpoTabelaQuarto').append(lin);
        }
    }casaista de mobilias retornadas; 
        for (var i in mobilia) { //i vale a posição no vetor
            lin = '<tr>' + // elabora linha com os dados da mobilia
                '<td>' + mobilia[i].nome + '</td>' +
                '<td>' + mobilia[i].funcao + '</td>' +
                '<td>' + mobilia[i].material + '</td>' +
                '<td>' + mobilia[i].quarto + '</td>' +
                '</tr>';
            // adiciona a linha no corpo da tabela
            $('#corpoTabelaMobilia').append(lin);
        }//
    }

});
*/
});