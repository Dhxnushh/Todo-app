function send(event){
    event.preventDefault();
    var task = document.getElementById("task");
    let date = new Date();
    let time = date.toLocaleTimeString();
    if(task.value===""){
        return;
    }
    content = `
    <li style="font-size:2em; text-align: left;"><span>${task.value}</span><span id="time";">${time}</span></li>
    `
    console.log(task)
    document.getElementById("display").innerHTML+=content;
    task.value="";
}
