const express = require('express');
const app = express();

app.get("/infinito", function(req, res){
    let i = 0
   /*  while(i <= 10000){
        console.log(i++)
    } */
    setInterval(function(){ //Callback (async)
        console.log(i++)
    },50)
})
app.get("/data", function(req, res){
    res.json({
        date: new Date()
    })
})
app.listen(80)