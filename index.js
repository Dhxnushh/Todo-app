function send(){
    var task = document.getElementById("task");
    content = `
    <li style="font-size:2em; text-align: left;">${task.value}</li>
    `
    console.log(task)
    document.getElementById("display").innerHTML+=content;
    task.value="";
}