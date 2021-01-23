document.getElementById('login_btn').addEventListener('click', function(){
    document.querySelector('.full-loginpage').style.display = 'flex';
})
document.querySelector('.close').addEventListener('click', function(){
    document.querySelector('.full-loginpage').style.display = 'none';
})