fetch("http://127.0.0.1:5000/music/list")
    .then(response=>response.json())
    .then(data=>{
       let place="{{url_for('static',filename='music/"
       let music=""
       let audio=document.getElementsByTagName("audio")
       if(audio[0].muted==true){
            audio[0].play()
       } else{
        audio[0].play()
       }
       let order=document.getElementsByTagName("ol")
       for(let i=0;i<data.length;i++){
        music+="<li>"+data[i].split(".m")[0]+"</li>"
       }
       order[0].innerHTML=music
       let list=document.getElementsByTagName("li")
       for(let i=0;i<list.length;i++){
            list[i].addEventListener("click",function(){
               audio[0].pause()
               audio[0].src=place+data[i]+"')}}"
               audio[0].play()
            })
       }
       
    }).catch(err=>{
        console.error(err)
    })                                  