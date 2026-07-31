// src/components/ChapterPage.js
import { createMetricCard } from './MetricCard.js';
import { createCalculator } from './Calculator.js';
import { createAlgorithmFlow } from './AlgorithmFlow.js';

export function createChapterPage(chapter, guidelineMap) {
  const page = document.createElement('div');
  page.className = 'chapter-page';
  
  const title = document.createElement('h2');
  title.textContent = chapter.title;
  title.style.marginBottom = '2rem';
  title.style.borderBottom = '1px solid var(--glass-border)';
  title.style.paddingBottom = '0.5rem';
  page.appendChild(title);

  const metricsList = document.createElement('div');
  metricsList.className = 'metric-list';

  chapter.metrics.forEach(metric => {
    if (metric.type === 'reference' || !metric.type) {
      const card = createMetricCard(metric, guidelineMap);
      metricsList.appendChild(card);
    } else if (metric.type === 'calculator') {
      const card = createMetricCard(metric, guidelineMap, false); // No table needed initially
      const calc = createCalculator(metric);
      card.querySelector('.metric-content').appendChild(calc);
      metricsList.appendChild(card);
    } else if (metric.type === 'algorithm') {
      const card = createMetricCard(metric, guidelineMap, false);
      const flow = createAlgorithmFlow(metric);
      card.querySelector('.metric-content').appendChild(flow);
      metricsList.appendChild(card);
    }
  });

  page.appendChild(metricsList);
  return page;
}
