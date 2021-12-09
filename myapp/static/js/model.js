// Model catalog

const modelBasket = document.querySelector('.catalog__model'),
      modelBtn = document.querySelectorAll('.catalog__item-btn'),
      closeCat = document.querySelector('.catalog__close');
      body = document.querySelector('body');

    modelBtn.forEach(function (item) {
        item.addEventListener('click', function() {
            modelBasket.style.display = 'flex';
        
            body.classList.add('active-over');
        });
    });

    closeCat.addEventListener('click', function () {
        modelBasket.style.display = 'none';
        body.classList.remove('active-over');
    });


// Model reviews
const modelReviews = document.querySelector('.reviews__model'),
      modelBtnRw = document.querySelector('.add-reviews'),
      closeCatRw = document.querySelector('.reviews__close');
      body = document.querySelector('body');


modelBtnRw.addEventListener('click', function() {
    modelReviews.style.display = 'flex';
    body.classList.add('active-over');
});

closeCatRw.addEventListener('click', function () {
    modelReviews.style.display = 'none';
    body.classList.remove('active-over');
});



