function soma(a, b, func_callback){
    setTimeout(function (){
        func_callback(a + b)
    }, 1000)
}

const result = soma(2,2, function(total) {
    console.log('Total: ' + total)
    soma(total, 250, function(total){
        console.log('Total: '+ total)
        soma(total, 10, function(r){
            console.log('Total: '+ r)
        })
    })
})
console.log(result)