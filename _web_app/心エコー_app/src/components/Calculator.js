// src/components/Calculator.js
import { formulaRegistry } from '../utils/mathFormulas.js';

export function createCalculator(metric) {
  const def = metric.calculatorDef;
  const formula = formulaRegistry[def.formulaId];
  
  const container = document.createElement('div');
  container.className = 'calculator-container';
  container.style.marginTop = '1rem';
  container.style.padding = '1rem';
  container.style.background = 'rgba(0,0,0,0.2)';
  container.style.borderRadius = '8px';

  const form = document.createElement('form');
  form.className = 'calc-form';
  form.style.display = 'flex';
  form.style.flexDirection = 'column';
  form.style.gap = '1rem';

  const inputsMap = {};

  def.inputs.forEach(inp => {
    const group = document.createElement('div');
    group.style.display = 'flex';
    group.style.justifyContent = 'space-between';
    group.style.alignItems = 'center';

    const label = document.createElement('label');
    label.textContent = `${inp.label} (${inp.unit})`;
    label.style.fontSize = '0.9rem';

    const input = document.createElement('input');
    input.type = 'number';
    input.step = 'any';
    input.style.width = '120px';
    input.style.padding = '0.5rem';
    input.style.borderRadius = '4px';
    input.style.border = '1px solid var(--glass-border)';
    input.style.background = 'var(--card-bg)';
    input.style.color = '#fff';

    inputsMap[inp.id] = input;

    group.appendChild(label);
    group.appendChild(input);
    form.appendChild(group);
  });

  const resultsDiv = document.createElement('div');
  resultsDiv.className = 'calc-results';
  resultsDiv.style.marginTop = '1rem';
  resultsDiv.style.paddingTop = '1rem';
  resultsDiv.style.borderTop = '1px solid var(--glass-border)';

  const updateResults = () => {
    const vals = {};
    for (const [id, el] of Object.entries(inputsMap)) {
      const val = parseFloat(el.value);
      vals[id] = isNaN(val) ? null : val;
    }
    const results = formula(vals);
    
    resultsDiv.innerHTML = '';
    if (results) {
      def.outputs.forEach(out => {
        if (results[out.id] !== undefined) {
          const resText = document.createElement('div');
          resText.style.fontWeight = 'bold';
          resText.style.color = 'var(--accent-color)';
          resText.style.fontSize = '1.2rem';
          resText.textContent = `${out.label}: ${results[out.id]} ${out.unit}`;
          resultsDiv.appendChild(resText);
        }
      });
    } else {
      const msg = document.createElement('div');
      msg.textContent = '数値を入力してください';
      msg.style.color = 'var(--text-muted)';
      msg.style.fontSize = '0.9rem';
      resultsDiv.appendChild(msg);
    }
  };

  form.addEventListener('input', updateResults);
  updateResults();

  container.appendChild(form);
  container.appendChild(resultsDiv);
  return container;
}
