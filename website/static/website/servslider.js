const slider = document.querySelector('.slider');
const slides = document.querySelector('.slides');
const dots = document.querySelectorAll('.dot');

let slideWidth = slider.clientWidth;
let currentSlide = 0;

function showSlide(slideIndex) {
  slides.style.transform = `translateX(-${slideIndex * slideWidth}px)`;

  dots.forEach((dot, index) => {
    dot.classList.toggle('active', index === slideIndex);
  });
}

function nextSlide() {
  currentSlide = (currentSlide + 1) % 3;
  showSlide(currentSlide);
}

function prevSlide() {
  currentSlide = (currentSlide - 1 + 3) % 3;
  showSlide(currentSlide);
}


window.addEventListener('resize', () => {
  slideWidth = slider.clientWidth;
  showSlide(currentSlide);
});


setInterval(nextSlide, 5000); // Slide every 5 seconds


dots.forEach((dot, index) => {
  dot.addEventListener('click', () => {
    showSlide(index);
    currentSlide = index;
  });
});