// monitoramento: localizacao

function monitoramento_pegar_bacia() {
    $.ajax({
        type: 'POST',
        url: '/monitoramento/',
        data: {
            bacia: $("select[name='bacia']").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            var options = '<option>Selecione um rio</option>';
            for (var i = 0; i < data.length; i++) {
                options += '<option value="' + data[i].pk + '">' + data[i].fields['nome'] + '</option>';
                console.log(options)
            }
            $("select#rio").html(options);
            $("select#rio").attr('disabled', false);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}

function monitoramento_pegar_rio() {
    $.ajax({
        type: 'POST',
        url: '/monitoramento/',
        data: {
            rio: $("select[name='rio']").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            var options = '<option>Selecione um ponto</option>';
            for (var i = 0; i < data.length; i++) {
                latlong = 'Latitude: ' + data[i].fields['latitude'] + ' -  Longitude:  ' + data[i].fields['longitude'];
                options += '<option value="' + data[i].pk + '">' + latlong + '</option>';
                console.log(options)
            }
            $("select#ponto").html(options);
            $("select#ponto").attr('disabled', false);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}

function monitoramento_pegar_ponto() {
    $.ajax({
        type: 'POST',
        url: '/monitoramento/',
        data: {
            ponto: $("select[name='ponto']").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            var options = '<option>Selecione uma data</option>';
            for (var i = 0; i < data.length; i++) {
                options += '<option value="' + data[i].pk + '">' + data[i].fields['data_monitoramento'] + '</option>';
                console.log(options)
            }
            $("select#data").html(options);
            $("select#data").attr('disabled', false);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}

//
// rio
//

function rio_pesquisar_bacia() {
    $.ajax({
        type: 'POST',
        url: '/rio/',
        data: {
            bh: $("select[name='bh']").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            var rios = '';
            for (var i = 0; i < data.length; i++) {
                rios += '<tr> <td>' + data[i].fields['nome'] + '</td> <td>' + data[i].fields['dimensao'] + '</td> <td>' + data[i].fields['bacia_hidrografica'] + '</td> <td> <a href="/rio/edit/' + data[i].pk + '/" class="btn btn-info">Editar</a> <a href="/rio/delete/' + data[i].pk + '/" class="btn btn-info">Excluir</a></td> </tr>';
                console.log(rios)
            }
            $("tbody#tbrio").html(rios);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}

//
// ponto
//

function ponto_pesquisar_rio() {
    $.ajax({
        type: 'POST',
        url: '/ponto/',
        data: {
            ponto: $("select[name='ponto']").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            var pontos = '';
            for (var i = 0; i < data.length; i++) {
                pontos += '<tr> <td>' + data[i].fields['latitude'] + '</td> <td>' + data[i].fields['longitude'] + '</td> <td> <a href="/ponto/edit/' + data[i].pk + '/" class="btn btn-info">Editar</a> <a href="/ponto/delete/' + data[i].pk + '/" class="btn btn-info">Excluir</a></td> </tr>';
                console.log(pontos)
            }
            $("tbody#pontos").html(pontos);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}

function ponto_pesquisar_bacia() {
    $.ajax({
        type: 'GET',
        url: '/ponto/add/',
        data: {
            bh: $("select[name='bh']").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            var options = '<option>Selecione uma bacia hidrográfica</option>';
            for (var i = 0; i < data.length; i++) {
                options += '<option value="' + data[i].pk + '">' + data[i].fields['nome'] + '</option>';
                console.log(options)
            }
            $("select#rio").html(options);
            $("select#rio").attr('disabled', false);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}

//
// coleta
//

function coleta_pesquisar_bacia() {
    $.ajax({
        type: 'GET',
        url: '/coleta/add/',
        data: {
            bh: $("select[name='bh']").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            var options = '<option>Selecione um rio</option>';
            for (var i = 0; i < data.length; i++) {
                options += '<option value="' + data[i].pk + '">' + data[i].fields['nome'] + '</option>';
                console.log(options)
            }
            $("select#rio").html(options);
            $("select#rio").attr('disabled', false);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}

function coleta_pesquisar_rio() {
    $.ajax({
        type: 'GET',
        url: '/coleta/add/',
        data: {
            rio: $("select[name='rio']").val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        dataType: 'json',
        success: function (data) {
            var options = '<option>Selecione um ponto</option>';
            for (var i = 0; i < data.length; i++) {
                latlong = 'Latitude: ' + data[i].fields['latitude'] + ' -  Longitude:  ' + data[i].fields['longitude'];
                options += '<option value="' + data[i].pk + '">' + latlong + '</option>';
                console.log(options)
            }
            $("select#ponto_monitoramento").html(options);
            $("select#ponto_monitoramento").attr('disabled', false);
        },
        error: function (xhr, errmsg) {
            console.log(xhr.status + ": " + xhr.responseText + "Error: " + errmsg);
        }
    });
}

