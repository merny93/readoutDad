function openFolderHandler() {
    if (this.responseText) {
        var response = JSON.parse(this.responseText);
        document.getElementById("open-folder-container").innerHTML = 'Selected directory: ' + response.directory;
    }
}

function openFolder() {
    doAjax("/choose/path", "POST", openFolderHandler);
}
var xy;
function getFields() {
    inputs = document.getElementsByTagName('input');
    console.log(inputs)
    xy = inputs;
    var fields = new Object();
    for (let index = 0; index < inputs.length; index++) {
        fields[index] = inputs[index].id;   
        console.log(fields[index])
    }
    return fields
}

function prevValFiller(response) {
    //will print the result field to 
    if (this.responseText) {
        var response = JSON.parse(this.responseText);
        for (var key in response){
            document.getElementById(key).value = response[key];
        }
    }

}

 
function triggerPreFill(){
    var stuff = getFields();
    console.log(stuff)
    doAjax("/get/vals", "POST", prevValFiller, stuff)
}

document.addEventListener("DOMContentLoaded", triggerPreFill);

var xx;

function submit() {
    //first get values and concatinate them

    var valHolder = new Object();

    var fields = getFields()
    xx = fields
    for (key in fields) {
        valHolder[fields[key]] =  document.getElementById(fields[key]).value;        
    }

    doAjax("/values", "POST", doStuffHandler, valHolder);
}