document.addEventListener('DOMContentLoaded', function () {
  const track = document.querySelector('.approval-track');
  const items = track.querySelectorAll('.approval-item');
  const itemWidth = items[0].offsetWidth;

  setInterval(() => {
    track.scrollBy({ left: itemWidth, behavior: 'smooth' });
    // Check if at the end and reset to start
    setTimeout(() => {
      if (track.scrollLeft + track.clientWidth >= track.scrollWidth) {
        track.scrollTo({ left: 0, behavior: 'smooth' });
      }
    }, 500); // small delay to allow scroll to complete
  }, 4000);
});
