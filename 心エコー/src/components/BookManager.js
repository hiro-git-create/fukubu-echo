// src/components/BookManager.js
export function createBookManager(pages) {
  let currentIndex = 0;
  
  const container = document.createElement('div');
  container.className = 'book-container';
  
  const book = document.createElement('div');
  book.className = 'book';
  
  pages.forEach((page, index) => {
    page.classList.add('page');
    if (index === 0) page.classList.add('active');
    else if (index === 1) page.classList.add('next-page');
    book.appendChild(page);
  });
  
  container.appendChild(book);
  
  const controls = document.createElement('div');
  controls.className = 'book-controls';
  
  const prevBtn = document.createElement('button');
  prevBtn.className = 'book-btn prev-btn';
  prevBtn.textContent = '◀ 前のページ';
  prevBtn.disabled = true;
  
  const nextBtn = document.createElement('button');
  nextBtn.className = 'book-btn next-btn';
  nextBtn.textContent = '次のページ ▶';
  
  if (pages.length <= 1) nextBtn.disabled = true;

  const updatePages = () => {
    pages.forEach((page, index) => {
      page.className = 'page'; // reset
      if (index < currentIndex) {
        page.classList.add('flipped');
      } else if (index === currentIndex) {
        page.classList.add('active');
      } else if (index === currentIndex + 1) {
        page.classList.add('next-page');
      }
    });
    
    prevBtn.disabled = currentIndex === 0;
    nextBtn.disabled = currentIndex === pages.length - 1;
  };

  prevBtn.addEventListener('click', () => {
    if (currentIndex > 0) {
      currentIndex--;
      updatePages();
    }
  });

  nextBtn.addEventListener('click', () => {
    if (currentIndex < pages.length - 1) {
      currentIndex++;
      updatePages();
    }
  });
  
  controls.appendChild(prevBtn);
  controls.appendChild(nextBtn);
  
  const doJump = (idx) => {
    if (idx >= 0 && idx < pages.length) {
      currentIndex = idx;
      updatePages();
    }
  };
  
  return { container, controls, updatePages, doJump };
}
