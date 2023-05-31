a = 10 //Tipo number inteiro
console.log(a + " - " + typeof(a))

a = 20.5 //Tipo number decimal
console.log(a + " - " + typeof(a))

console.log('a == 20.5' + a == 20.5) //compara o tipo
console.log('a == "20.5"' + a == "20.5") //compara o tipo
console.log('a === "20.5"' + a === "20.5") //verifica o conteúdo
// Tipo texto
a = "zezinho"
console.log(a + " - " + typeof(a))
// Tipo lógico
a = true
console.log(a + " - " + typeof(a))
console.log("São iguais: " + (a == "1"))
// Tipo lista
nomes = ['zezinho', 'Joãozinho', 'Luizinho']
console.log(nomes[0])
console.log(nomes[1])
console.log(nomes[2])
console.log(nomes + " - " + typeof(nomes))
// Tipo objeto
pessoa = new Object();
pessoa.nome = "zezinho"
pessoa.idade = 22
console.log(pessoa + " - " + typeof(pessoa))
// Tipo função
meuCodigo = function(){
    console.log("Opa!")
}
meuCodigo()
console.log(meuCodigo + " - " + typeof(meuCodigo))

valor = 0
console.log(valor++)
// Operador de incremento POS FIXADO
console.log(++valor)
// Operador de incremento PRÉ FIXADO

cont = 0
while(cont <= 10){
    console.log(cont)
    //cont = cont + 1   #Python
    //cont += 1         #Python
    cont ++             //JS
}

cont = 10
do{
    console.log("Rodando...")
    cont ++
}while(cont <= 10)

for (i=0;i<=10;i++){
    console.log("Contado: " + i)
}