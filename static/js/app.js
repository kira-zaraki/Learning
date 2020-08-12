window.onload = function(){
    button = document.getElementsByClassName('add_page_to_section')[0]
    nav = document.getElementsByClassName('nav_page')[0]
    button.addEventListener('click', e => {
        var element = document.createElement('input')
        console.log(button.closest('div').lastChild)
        nav.appendChild(element)
    })
}