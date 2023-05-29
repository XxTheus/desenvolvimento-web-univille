var refDisplay = document.getElementById('display')

function botaoClicado(numero){
    console.log(numero);
    refDisplay.value += numero
}

function limparTudo(){
    refDisplay.value = ''
}

function limparUm(){
    refDisplay.value = refDisplay.value.substring(0, refDisplay.value.length - 1)
}

function resultado(){
    refDisplay.value = eval(refDisplay.value)
}