function soma(a, b){
    setTimeout(function (){
        return a + b
    }, 1000)
    //return undefined (implicito)
}

const result = soma(2,2)
console.log(result)