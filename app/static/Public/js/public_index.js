document.getElementById('login_btn').addEventListener('click', function(){
    document.querySelector('.full-loginpage').style.display = 'flex';
})
document.querySelector('.close').addEventListener('click', function(){
    document.querySelector('.full-loginpage').style.display = 'none';
})

function myFunction() {
    var x = document.getElementById("showpassbtn");
    if (x.type === "password") {
        x.type = "text";
    } else {
        x.type = "password";
    }
}

console("hie how are lkyou")