document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('#likes_users').forEach(element => element.style.display = 'none');
    document.querySelectorAll('#likes_amount').forEach(element => element.addEventListener('click', show_likes));
    document.querySelector('#edit').addEventListener('click', load_edit);
    document.querySelector('#edit_profile').style.display = 'none';
    document.querySelector('#likes').addEventListener('click', show_likes);

})

function load_edit(){
    document.querySelector('.profile_div').style.display = 'none';
    document.querySelector('#edit_profile').style.display = 'block';
    console.log("hello it's working")
}
function show_likes(){
    document.addEventListener('click', event =>{
        event.target.style.display = 'none';
        event.target.parentElement.style.display = 'none';
    })
}