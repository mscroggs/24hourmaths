<div id="signup">
<input type="email" id="email">
<button onpress="sign_me_up()">Sign me up!</button>
</div>

<script type='text/javascript'>
function sign_me_up(){
    var sender;
    if(window.XMLHttpRequest){sender=new XMLHttpRequest();}
    else {sender=new ActiveXObject('Microsoft.XMLHTTP');}
    sender.open("POST", "https://mscroggs.co.uk/24hr.php");
    sender.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    sender.setRequestHeader("crossDomain", true);
    sender.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        alert(this.reponseText)
        document.getElementById("signup").innerHTML = "Signed up. We'll be in touch!"
      }
    }
    sender.send("email="+document.getElementById("email"));
    document.getElementById("signup").innerHTML = "Signing up..."
    return false;
}
</script>
