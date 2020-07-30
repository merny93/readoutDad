const interval = setInterval(function() {
    doAjax('/monitor/refresh', "GET", monitorHandler)
}, 1000);


function monitorHandler(response) {
    if (this.responseText){
        var response = JSON.parse(this.responseText);
        document.getElementById('time-box').innerHTML = response.time;
        var vals = response.vals
        for (var key in vals){
            if (!document.getElementById(key)){
                var newInput = document.createElement("INPUT");
                newInput.id = key;
                //newInput.type = "text";
                newInput.value = vals[key];
                var newLabel = document.createElement("Label");
                newLabel.htmlFor = key;
                newLabel.innerHTML = key;
                document.getElementById("monitor-holder").appendChild(newLabel);
                document.getElementById("monitor-holder").appendChild(newInput);
            } else{
                document.getElementById(key).value = vals[key];
            }
        }
    }
}

document.addEventListener("load",doAjax('/monitor/refresh', "GET", monitorHandler))
// function getFields() {
//     inputs = document.getElementById('monitor-holder').children;
//     console.log(inputs)
//     var fields = new Object();
//     for (let index = 0; index < inputs.length; index++) {
//         fields[index] = inputs[index].id;   
//         console.log(fields[index])
//     }
//     return fields
// }
