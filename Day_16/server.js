const fs=require('fs');
fs.readFile('hello.txt','utf-8',(err,data)=>{
    if(err) throw err;
    console.log(data);
})
//const server = http.createServer((req,res) => {
//    res.statusCode = 200;
//    res.setHeader('Content-Type','text/html');
//    res.end('<h1>Hello, World!</h1>')
//})