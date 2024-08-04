fetch("http://127.0.0.1:5000/music/list")
    .then(response=>response.json())
    .then(data=>{
        let music=""
       let order=document.getElementsByTagName("ol")
       for(let i=0;i<data.length;i++){
        music+="<li>"+data[i]+"</li>"
       }
       order[0].innerHTML=music
    }).catch(err=>{
        console.error(err)
    })                                  