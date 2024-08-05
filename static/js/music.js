fetch("http://127.0.0.1:5000/music/list")
    .then(response=>response.json())
    .then(data=>{
       let place="/static/music/"
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
       let p=0
       for(let i=0;i<list.length;i++){
            list[i].addEventListener("click",function(){
               audio[0].pause()
               audio[0].src=place+data[i]
               audio[0].play()
               p=i+1
               document.getElementsByTagName("h3")[0].innerText="playing "+p
               
          })
       }
       
       audio[0].addEventListener("ended",function(){
          if(p+1<28){
               audio[0].pause()
               audio[0].src=place+data[p+1]
               audio[0].play()
               p=i+1
               document.getElementsByTagName("h3")[0].innerText="playing "+p
               
          } else if(p==28){
               audio[0].pause()
               audio[0].src=place+data[0]
               audio[0].play()
               p=1
               document.getElementsByTagName("h3")[0].innerText="playing "+p
               
          }
       })
               
    }).catch(err=>{
        console.error(err)
    })                                  