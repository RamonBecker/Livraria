
$('#abrir').onload(function(event){
  bootbox.alert('Oi, eu sou um alert.');
});

window.onsubmit = function clickTest(){
    bootbox.alert('Atenção ! Voce precisa cadastrar pelo menos uma editora.')
}