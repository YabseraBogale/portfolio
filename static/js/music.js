fetch("http://127.0.0.1:5000/music/list")
    .then(response=>response.json())
    .then(data=>{
        console.log(data)
    }).catch(err=>{
        console.error(err)
    })                                  