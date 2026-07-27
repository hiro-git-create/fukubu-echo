export function createSearchBar(onSearch) {
  const container = document.createElement('div');
  container.className = 'search-container';

  const input = document.createElement('input');
  input.type = 'text';
  input.className = 'search-input';
  input.placeholder = '指標名 (例: LVDd, EF) を検索...';
  
  let timeoutId;
  input.addEventListener('input', (e) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
      onSearch(e.target.value);
    }, 300);
  });

  container.appendChild(input);
  return container;
}
