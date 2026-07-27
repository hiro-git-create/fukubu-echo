// src/components/AlgorithmFlow.js
export function createAlgorithmFlow(metric) {
  const container = document.createElement('div');
  container.className = 'algorithm-container';
  container.style.marginTop = '1rem';
  container.style.background = 'rgba(255,255,255,0.05)';
  container.style.borderRadius = '8px';
  container.style.padding = '1rem';

  const title = document.createElement('h4');
  title.textContent = '評価フローチャート';
  title.style.marginBottom = '1rem';
  title.style.fontSize = '1rem';
  container.appendChild(title);

  const steps = metric.evaluationFlow.steps;
  const flowDiv = document.createElement('div');
  flowDiv.style.display = 'flex';
  flowDiv.style.flexDirection = 'column';
  flowDiv.style.gap = '0.5rem';

  steps.forEach((step, idx) => {
    const stepCard = document.createElement('div');
    stepCard.style.padding = '0.75rem';
    stepCard.style.background = 'var(--card-bg)';
    stepCard.style.border = '1px solid var(--glass-border)';
    stepCard.style.borderRadius = '6px';
    
    const condLabel = document.createElement('div');
    condLabel.style.fontWeight = 'bold';
    condLabel.style.color = 'var(--accent-color)';
    condLabel.textContent = `Step ${idx + 1}: ${step.condition}`;
    
    const resultLabel = document.createElement('div');
    resultLabel.style.fontSize = '0.875rem';
    resultLabel.style.marginTop = '0.25rem';
    if (step.next) {
      resultLabel.textContent = `→ Next: ${step.next}`;
    } else if (step.result) {
      resultLabel.textContent = `→ Result: ${step.result}`;
      resultLabel.style.color = '#ff7b72'; // A reddish color for final result
    }

    stepCard.appendChild(condLabel);
    stepCard.appendChild(resultLabel);
    flowDiv.appendChild(stepCard);

    if (idx < steps.length - 1) {
      const arrow = document.createElement('div');
      arrow.textContent = '↓';
      arrow.style.textAlign = 'center';
      arrow.style.color = 'var(--text-muted)';
      flowDiv.appendChild(arrow);
    }
  });

  container.appendChild(flowDiv);
  return container;
}
