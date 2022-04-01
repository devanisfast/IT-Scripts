console.log("Custom Script");

const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const records= urlParams.get('records');

if(records == 1){
    console.log("#####Running Records Management script here#####");

    window.onload = function(){
        document.getElementsByClassName("inputMultipleSelectOptionTitle")[11].click()
        document.getElementsByClassName("inputMultipleSelectOptionTitle")[13].click()
        document.getElementById("button_continue").click()
      };
}
if(records == 2){
    console.log("#####Running Records Management script here#####");
      
    window.onload = function(){
        document.getElementsByClassName("inputMultipleSelectOptionTitle")[11].click()
        document.getElementsByClassName("inputMultipleSelectOptionTitle")[14].click()
        document.getElementById("button_continue").click()
      };
}
