function serialHandler(response) {
    if (this.responseText) {
        var response = JSON.parse(this.responseText);
        document.getElementById("connectionStatus").innerHTML = response.result;
    }

}



function checkConnection() {
    doAjax("/connection", "POST", serialHandler);
}
