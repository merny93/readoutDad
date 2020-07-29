function doStuffHandler(response) {
    if (this.responseText) {
        var response = JSON.parse(this.responseText);
        document.getElementById("stuff-container").innerHTML = response.result;
    }

}

function toggleFullscreen() {
    doAjax("/fullscreen", "POST", doStuffHandler);
}


