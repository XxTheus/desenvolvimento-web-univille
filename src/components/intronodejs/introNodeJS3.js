function infinito(){
    let i = 0
    //Callback function
    setInterval(function(){
            console.log(i++)
        }, 1000)
}
function data() {
    console.log(new Date())
}
infinito()
data()