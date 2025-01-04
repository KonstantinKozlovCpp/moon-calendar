// Загрузка данных из moon_phases.json
fetch('moon_phases.json')
    .then(response => response.json())
    .then(moonPhases => {
        const tbody = document.querySelector('#moon-calendar tbody');
        moonPhases.forEach(item => {
            const row = document.createElement('tr');
            row.innerHTML = `<td>${item.date}</td><td>${item.phase}</td>`;
            tbody.appendChild(row);
        });
    })
    .catch(error => console.error("Ошибка при загрузке данных: ", error));
