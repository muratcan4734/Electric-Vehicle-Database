function comparing_checked_boxes(){
    const elements = Array.from(document.querySelectorAll("input[type=checkbox]"));
    const compare_button_element = document.getElementById("compare_button");

    var check_boxes = 0;

    for (var i = 0; i < elements.length; i++) {

        if (elements[i].checked == true){
            check_boxes = check_boxes + 1;
        }
    }

     if(check_boxes >= 2){

        compare_button_element.hidden = false;
    } else {
        compare_button_element.hidden = true;
    }
}
firebase.auth().onAuthStateChanged(function(user) {

    if(!user){
        location.replace("/")
    }
})