import { createGuidelineTable } from './GuidelineTable.js';

export function createMetricCard(metric, guidelineMap, showTable = true) {
  const card = document.createElement('div');
  card.className = 'metric-card';

  const header = document.createElement('div');
  header.className = 'metric-header';
  
  const titleInfo = document.createElement('div');
  titleInfo.className = 'metric-title-info';
  
  const title = document.createElement('div');
  title.className = 'metric-title';
  
  const spanAbbr = document.createElement('span');
  spanAbbr.className = 'metric-abbr';
  spanAbbr.textContent = metric.abbreviation;
  
  const spanName = document.createElement('span');
  spanName.className = 'metric-name';
  spanName.textContent = metric.name;
  
  title.appendChild(spanAbbr);
  title.appendChild(spanName);

  const desc = document.createElement('div');
  desc.className = 'metric-desc';
  desc.textContent = metric.description;

  titleInfo.appendChild(title);
  titleInfo.appendChild(desc);

  const icon = document.createElement('div');
  icon.className = 'metric-icon';
  icon.textContent = '▾'; // Down arrow character

  header.appendChild(titleInfo);
  header.appendChild(icon);

  const content = document.createElement('div');
  content.className = 'metric-content';
  
  if (metric.unit) {
    const unitInfo = document.createElement('p');
    unitInfo.style.marginBottom = '1rem';
    unitInfo.style.fontSize = '0.875rem';
    unitInfo.style.color = 'var(--text-muted)';
    unitInfo.textContent = `単位: ${metric.unit}`;
    content.appendChild(unitInfo);
  }

  if (showTable && metric.references) {
    const table = createGuidelineTable(metric.references, guidelineMap);
    content.appendChild(table);
  }

  card.appendChild(header);
  card.appendChild(content);

  // Toggle expansion
  header.addEventListener('click', () => {
    card.classList.toggle('expanded');
  });

  return card;
}
