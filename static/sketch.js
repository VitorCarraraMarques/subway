function findPath(){ 
    let source = $("#source").val();
    let dest = $("#dest").val();
    console.log("FROM HTML -> source-type: ", typeof source, " dest_type: ",  typeof dest);
    $.ajax("http://127.0.0.1:8800/find-path", {
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({"source": source, "dest": dest}),
        success: (data,status) => displayPath(data),
    });
}
  
function displayPath(data){
    let path = data.path;
    console.log(path.length);;
    const sect = document.querySelector("#data-output"); 
    const para = document.createElement("p"); 
    let dataText = path[0][0];
    for (let i = 1; i < path.length; i++){
        dataText += " -> " + path[i][0];
        console.log(path[i][0]);
    }
    para.textContent = dataText; 
    sect.appendChild(para); 
}


    