//Função anônimo e auto executável
//Função = Bloco de código com nome
// var = variável hoisting (elevação/içamento) *Joga a variável para cima da aplicação*
void function() {
    console.log(mensagem) 
}()
var mensagem = "Teste" //hoisting

console.log("______________________")

function soma (a, b){
    return a + b
}

var resultado = soma(2,2)
console.log(resultado)

console.log("______________________")

var exibeMsn = function(){
    if(true){
        var escopoFuncao = 'Caelum' //Escopo global (Disponível em todo programa)
        let escopoBloco = 'Alura' //Escopo local (Somente dentro do bloco)
        console.log(escopoBloco)
    }
    console.log(escopoFuncao)
}
/* console.log(exibeMsn) */
exibeMsn()

console.log("______________________")

//const - cria constantes
void function() {
    const msg = 'Alura' 
    console.log(msg)
    //msg = 'Caelum'
}()

console.log("______________________")

let estado = 'SC'
switch (estado){
    case 'SC': case 'sc':
        console.log('Santa Catarina')
    break
    case 'PR': case 'pr':
        console.log("Paraná")
    break
    default:
        console.log('Não definido')
}

console.log("______________________")

cont = 0
while (cont <= 10){
    console.log(cont)
    cont++
}

console.log("______________________")

let quandoVale = 0
console.log(quandoVale++)
console.log(++quandoVale)

console.log("______________________")

let i = 10
do{
    console.log("Entrou")
}while(i < 10)

console.log("______________________")