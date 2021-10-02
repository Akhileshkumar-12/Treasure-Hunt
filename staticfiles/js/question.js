let questions = [{
        id: 1,
        question: "What is the full form of RAM ?",
        answer: "Random Access Memory",
        options: [
            "Random Access Memory",
            "Randomely Access Memory",
            "Run Aceapt Memory",
            "None of these"
        ] 
    },
    {
        id: 2,
        question: "What is the full form of CPU?",
        answer: "Central Processing Unit",
        options: [
            "Central Program Unit",
            "Central Processing Unit",
            "Central Preload Unit",
            "None of these"
        ]
    },
    {
        id: 3,
        question: "What is the full form of E-mail",
        answer: "Electronic Mail",
        options: [
            "Electronic Mail",
            "Electric Mail",
            "Engine Mail",
            "None of these"
        ]
    }
];




let question_count = 0;
let points = 0;

window.onload = function() {
    show(question_count);

};

function next() {


    // if the question is last then redirect to final page
    if (question_count == questions.length - 1) {
        // sessionStorage.setItem("time", time);
        // clearInterval(mytime);
        location.href = "end.html";
    }
    // console.log(question_count);
    let initQues = document.querySelector("#quesNo");
    initQues.innerHTML = `${question_count + 2} `;
    

    let user_answer = document.querySelector("li.option.active").innerHTML;
    // check if the answer is right or wrong
    if (user_answer == questions[question_count].answer) {
        points += 10;
        sessionStorage.setItem("points", points);
    }
    // console.log(points);
    let scoremark = document.getElementById("score");
    scoremark.innerHTML = `${points}`;

    question_count++;
    show(question_count);
}

function skip() {
    question_count++;
    show(question_count);

    if (question_count == questions.length - 1) {
        sessionStorage.setItem("time", time);
        // clearInterval(mytime);
        location.href = "end.html";
    }
}

function show(count) {
    let question = document.getElementById("questions");
    let [first, second, third, fourth] = questions[count].options;

    question.innerHTML = `
    <h5>Q${count + 1}. ${questions[count].question}</h5>
     <ul class="option_group">
    <li class="option">${first}</li>
    <li class="option">${second}</li>
    <li class="option">${third}</li>
    <li class="option">${fourth}</li>
  </ul> 
    `;
    toggleActive();
}

function toggleActive() {
    let option = document.querySelectorAll("li.option");
    for (let i = 0; i < option.length; i++) {
        option[i].onclick = function() {
            for (let i = 0; i < option.length; i++) {
                if (option[i].classList.contains("active")) {
                    option[i].classList.remove("active");
                }
            }
            option[i].classList.add("active");
        };
    }
}

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