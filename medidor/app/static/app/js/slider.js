/* ════════════════════════════════════════════════════════════
   HERO SLIDER  ·  slider.js
   Archivo: app/static/app/js/slider.js

   Añadir UNA línea en base.html antes de </body>:
     <script src="{% static 'app/js/slider.js' %}"></script>

   Expone 3 funciones globales usadas en los onclick del HTML:
     sliderGoTo(n)  →  ir al slide n
     sliderNext()   →  avanzar
     sliderPrev()   →  retroceder

   No toca nada del menú ni de otros scripts del proyecto.
════════════════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', function () {

  /* ── Elementos ── */
  const track  = document.getElementById('heroTrack');
  const slides = document.querySelectorAll('.hero-slide');
  const dots   = document.querySelectorAll('.hs-dot');
  const total  = slides.length;

  /* Guard: si no hay slider en esta página, salir */
  if (!track || !total) return;

  let cur = 0;

  /* ── Render: mueve el track y actualiza clases activas ── */
  function render() {
    track.style.transform = `translateX(-${cur * 100}%)`;
    slides.forEach((s, i) => s.classList.toggle('active', i === cur));
    dots.forEach((d, i)   => d.classList.toggle('active', i === cur));
  }

  /* ── Navegación ── */
  function next()  { cur = (cur + 1) % total;          render(); resetTimer(); }
  function prev()  { cur = (cur - 1 + total) % total;  render(); resetTimer(); }
  function goTo(i) { cur = i;                           render(); resetTimer(); }

  /* Exponer globalmente para los onclick inline del template */
  window.sliderGoTo = goTo;
  window.sliderNext = next;
  window.sliderPrev = prev;

  /* ── Autoplay: cambia cada 7 s ── */
  let timer;
  function resetTimer() {
    clearInterval(timer);
    timer = setInterval(next, 7000);
  }
  resetTimer();

  /* Pausa al hacer hover */
  const slider = document.querySelector('.hero-slider');
  if (slider) {
    slider.addEventListener('mouseenter', () => clearInterval(timer));
    slider.addEventListener('mouseleave', resetTimer);
  }

  /* ── Teclado ── */
  document.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowLeft')  prev();
    if (e.key === 'ArrowRight') next();
  });

  /* ── Swipe táctil ── */
  let touchX = 0;
  if (slider) {
    slider.addEventListener('touchstart', function (e) {
      touchX = e.touches[0].clientX;
    }, { passive: true });

    slider.addEventListener('touchend', function (e) {
      const dx = touchX - e.changedTouches[0].clientX;
      if (Math.abs(dx) > 45) dx > 0 ? next() : prev();
    });
  }

  /* Render inicial */
  render();

  /* ════════════════════════════════════════
     Reemplazar imagen del Slide 2 en runtime
     ════════════════════════════════════════
     Uso desde cualquier parte:
       setSlide2Image('/static/app/img/mi-foto.jpg');

     Uso desde un <input type="file">:
       document.getElementById('miInput').addEventListener('change', function(e) {
         setSlide2Image(URL.createObjectURL(e.target.files[0]));
       });
  ════════════════════════════════════════ */
  window.setSlide2Image = function (src) {
    const img = document.getElementById('s2img');
    if (img) img.src = src;
  };

});