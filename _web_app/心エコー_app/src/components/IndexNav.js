// src/components/IndexNav.js
export function createIndexNav(chapters, onNavClick) {
  const container = document.createElement('div');
  container.className = 'index-nav';
  
  const title = document.createElement('h2');
  title.textContent = '目次 (Index)';
  title.style.marginBottom = '2rem';
  container.appendChild(title);

  const list = document.createElement('ul');
  list.style.listStyle = 'none';
  list.style.display = 'flex';
  list.style.flexDirection = 'column';
  list.style.gap = '1rem';

  chapters.forEach((chapter, idx) => {
    const li = document.createElement('li');
    
    const btn = document.createElement('button');
    btn.className = 'index-btn';
    btn.textContent = chapter.title;
    btn.style.width = '100%';
    btn.style.padding = '1rem';
    btn.style.textAlign = 'left';
    btn.style.background = 'var(--card-bg)';
    btn.style.border = '1px solid var(--glass-border)';
    btn.style.borderRadius = '8px';
    btn.style.color = '#fff';
    btn.style.cursor = 'pointer';
    btn.style.fontSize = '1rem';
    btn.style.transition = 'transform 0.2s, background 0.2s';
    
    btn.addEventListener('mouseover', () => {
      btn.style.transform = 'translateY(-2px)';
      btn.style.background = 'var(--hover-bg)';
    });
    
    btn.addEventListener('mouseout', () => {
      btn.style.transform = 'none';
      btn.style.background = 'var(--card-bg)';
    });

    btn.addEventListener('click', () => {
      // index 0 is cover, 1 is index nav, so chapter 0 is page 2
      onNavClick(idx + 2);
    });

    li.appendChild(btn);
    list.appendChild(li);
  });

  container.appendChild(list);
  return container;
}
