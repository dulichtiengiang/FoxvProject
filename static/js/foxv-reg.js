// REGISTRATION
$(document).ready(function(){
    const form_Active = document.querySelector('.foxv-form-active');
    const btnNextf1 = document.querySelector('#foxv-btn-next-f1');
    const btnNextf2 = document.querySelector('#foxv-btn-next-f2');
    const btnNextf3 = document.querySelector('#foxv-btn-next-f3');

    const btnPrevf2 = document.querySelector('#foxv-btn-prev-f2');
    const btnPrevf3 = document.querySelector('#foxv-btn-prev-f3');
    const btnPrevf4 = document.querySelector('#foxv-btn-prev-f4');

    btnNextf1.addEventListener('click', function() {
        form_Active.style.marginLeft = '-25%';
    });
    btnNextf2.addEventListener('click', function() {
        form_Active.style.marginLeft = '-50%';
    });
    btnNextf3.addEventListener('click', function() {
        form_Active.style.marginLeft = '-75';
    });

    btnPrevf2.addEventListener('click', function() {
        form_Active.style.marginLeft = '0%';
    });
    btnPrevf3.addEventListener('click', function() {
        form_Active.style.marginLeft = '-25%';
    });
});