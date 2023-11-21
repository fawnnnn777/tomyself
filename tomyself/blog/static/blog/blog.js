document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('#edit').addEventListener('click', load_edit)
    document.querySelector('#edit_profile').style.display = 'none';

})

function load_edit(){
    document.querySelector('.profile_div').style.display = 'none';
    document.querySelector('#edit_profile').style.display = 'block';
    console.log("hello it's working")
}
