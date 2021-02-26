$(document).ready(function() {
/////////////////////////////////////////////
//////////Registration///////////////////////
/////////////////////////////////////////////
const form_Active = document.querySelector('.foxv-form-active');
const btnNextf1 = document.querySelector('#foxv-btn-next-f1');
const btnNextf2 = document.querySelector('#foxv-btn-next-f2');

const btnPrevf2 = document.querySelector('#foxv-btn-prev-f2');
const btnPrevf3 = document.querySelector('#foxv-btn-prev-f3');

btnNextf1.addEventListener('click', function() {
    form_Active.style.marginLeft = '-25%';
});
btnNextf2.addEventListener('click', function() {
    form_Active.style.marginLeft = '-50%';
});

btnPrevf2.addEventListener('click', function() {
    form_Active.style.marginLeft = '0%';
});
btnPrevf3.addEventListener('click', function() {
    form_Active.style.marginLeft = '-25%';
});
});