

const eventBox=document.getElementById('event-box')
const CountDownBox=document.getElementById('countdown-box')
// console.log(eventBox.textContent)
const Eventdate=Date.parse(eventBox.textContent)
// console.log(Eventdate)
setInterval(()=>{
    const now=new Date().getTime()
    // console.log(now)
    const diff=Eventdate-now
    // console.log(diff)
    const d=Math.floor(Eventdate/(1000*60*60*24)-(now/(1000*60*60*24)))
    const h=Math.floor((Eventdate/(1000*60*60)-(now/(1000*60*60)))%24)
    const m=Math.floor((Eventdate/(1000*60)-(now/(1000*60)))%60)
    const s=Math.floor((Eventdate/(1000)-(now/(1000)))%60)
    if(diff>0)
    {
        CountDownBox.innerHTML=m+":"+s
    }
    else
    {
        CountDownBox.innerHTML="00:00"
        document.getElementById("show").style.display = "none";
        document.getElementById("show1").style.display = "none";
        console.log("aman")
    }
},1000)

// function timeOut(){
//     if((`${minutes}` == 0 ) && (`${seconds}` == 0)){
//         location.href = "end.html";
//     }
// }