
const form = document.getElementById('ranking-form');
const status = document.getElementById('status');
const url = 'https://script.google.com/macros/s/AKfycbwaKAFi685f-1P3fsFkCA3BNKkkuJPCN601stiHF_UbnDhhPq_zykykIu-xeT2SiBQ3UA/exec';

const selects = [
  document.getElementById('choice1'),
  document.getElementById('choice2'),
  document.getElementById('choice3'),
];

fetch('data/projects.csv')
  .then(response => response.text())
  .then(csvText => {
    const results = Papa.parse(csvText.trim(), {
      header: true,
      skipEmptyLines: true,
      // no need to specify delimiter, defaults to ','
    });

    const projects = results.data;

    // Populate dropdown selects
    selects.forEach(select => {
      projects.forEach(project => {
        const el = document.createElement('option');
        el.value = project.ID;  // match your CSV header name exactly
        el.textContent = `${project.Projects} (${project.ID})`;
        select.appendChild(el);
      });
    });

    // Populate project table with three columns: Projects, ID, Quotas
    const tableBody = document.querySelector('#project-table tbody');
    projects.forEach(project => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td>${project.Projects}</td>
        <td>${project.ID}</td>
        <td>${project.Quotas || ''}</td>
      `;
      tableBody.appendChild(row);
    });
  });

form.addEventListener('submit', e => {
  e.preventDefault();

  const name = form.name.value.trim();
  const choice1 = form.choice1.value;
  const choice2 = form.choice2.value;
  const choice3 = form.choice3.value;

  if (new Set([choice1, choice2, choice3]).size < 3) {
    status.textContent = 'Please choose 3 different projects.';
    return;
  }

  const params = new URLSearchParams({
    name, choice1, choice2, choice3,
  });

  fetch(url, {
    method: 'POST',
    body: params,
  }).then(res => res.text())
    .then(() => {
      status.textContent = 'Submitted successfully!';
      form.reset();
    }).catch(err => {
      console.error(err);
      status.textContent = 'Error submitting your response.';
    });
});
