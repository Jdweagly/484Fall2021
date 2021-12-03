function formValidator(){
    var x = document.getElementById("username").value;
    var password1 =document.getElementById("password").value;
    var password2 =document.getElementById("verify").value;
    if(x.length < 6 ){
        alert("Username must be at least 6 characters long!");
        return false;
   }
        else if(x.length > 25){
         alert("Username must be less than 26 characters long!")
         return false;
     }
   if(password1 != password2){
    alert("Passwords do not match!");
    return false;
   }

   return true;
}	