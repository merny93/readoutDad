function doStuffHandler(response) {
    //will print the result field to 
    if (this.responseText) {
        var response = JSON.parse(this.responseText);
        if (typeof response.result != 'undefined'){
            document.getElementById("stuff-container").innerHTML = response.result;
        }
    }

}

function toggleFullscreen() {
    doAjax("/fullscreen", "POST", doStuffHandler);
}


