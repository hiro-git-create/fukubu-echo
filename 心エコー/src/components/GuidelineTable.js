export function createGuidelineTable(references, guidelineMap) {
  const table = document.createElement('table');
  table.className = 'guideline-table';

  const thead = document.createElement('thead');
  const trHead = document.createElement('tr');
  ['ガイドライン', '条件 (性別等)', '基準値'].forEach(text => {
    const th = document.createElement('th');
    th.textContent = text;
    trHead.appendChild(th);
  });
  thead.appendChild(trHead);
  table.appendChild(thead);

  const tbody = document.createElement('tbody');

  references.forEach(ref => {
    const guidelineName = guidelineMap[ref.guidelineId] || ref.guidelineId;

    ref.conditions.forEach((cond, index) => {
      const tr = document.createElement('tr');

      if (index === 0) {
        const tdGuideline = document.createElement('td');
        tdGuideline.rowSpan = ref.conditions.length;
        
        const span = document.createElement('span');
        span.className = 'guideline-id';
        span.textContent = ref.guidelineId;
        
        const br = document.createElement('br');
        
        const small = document.createElement('small');
        small.style.color = 'var(--text-muted)';
        small.textContent = guidelineName;
        
        tdGuideline.appendChild(span);
        tdGuideline.appendChild(br);
        tdGuideline.appendChild(small);
        tr.appendChild(tdGuideline);
      }

      const tdCond = document.createElement('td');
      let condText = cond.gender === 'male' ? '男性' : cond.gender === 'female' ? '女性' : '共通';
      if (cond.bsaAdjusted) condText += ' (BSA補正)';
      tdCond.textContent = condText;
      tr.appendChild(tdCond);

      const tdValue = document.createElement('td');
      const valSpan = document.createElement('span');
      valSpan.className = 'value-range';
      valSpan.textContent = `${cond.min} - ${cond.max}`;
      tdValue.appendChild(valSpan);
      tr.appendChild(tdValue);

      tbody.appendChild(tr);
    });
  });

  table.appendChild(tbody);
  return table;
}
