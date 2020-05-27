function openFolderHandler() {
    if (this.responseText) {
        var response = JSON.parse(this.responseText);
        document.getElementById("open-folder-container").innerHTML = 'Selected directory: ' + response.directory;
    }
}

function openFolder() {
    doAjax("/choose/path", "POST", openFolderHandler);
}

function submit() {
    //first get values and concatinate them
   
    var strs = new Array(3)
    var data_string = "";

    for (let index = 1; index <= strs.length; index++) {
        var ind = "v".concat(index.toString()); 
        if (index != strs.length) {
            var toAppend = document.getElementById(ind).value.concat("~");
            data_string = data_string.concat(toAppend);
        } else{
            data_string = data_string.concat(document.getElementById(ind).value);
        }
        
        
    }
    var toSend = "/values/".concat(data_string);
    doAjax(toSend, "POST", doStuffHandler);
}