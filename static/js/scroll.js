const cardWrapper = document.querySelector('.card-wrapper');
const scrollLeftBtn = document.querySelector('.scroll-left');
const scrollRightBtn = document.querySelector('.scroll-right');

scrollLeftBtn.addEventListener('click', () => {
  cardWrapper.scrollBy({ left: -250, behavior: 'smooth' });
});

scrollRightBtn.addEventListener('click', () => {
  cardWrapper.scrollBy({ left: 250, behavior: 'smooth' });
});