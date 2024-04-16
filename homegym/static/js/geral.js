function showLevel() {
    return fetch('http://127.0.0.1:5000/getlevel')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log(data)
            var level = data.level;
            var leveledUp = data.leveledUp;

            var container = $('#level');
            container.empty();
            var html = '<div class="leveltext">' + level + ' <i class="fa-solid fa-star" style="color: #ffc800;"></i></div>';
            container.append(html);

            if (leveledUp == 1) {
                Swal.fire({
                    title: 'Parabéns!',
                    text: 'Subiu para o Nivel ' + level + '',
                    icon: 'success',
                    timer: 4000,
                    showConfirmButton: false
                });
            }
        })
        .catch(error => {
            console.error('Fetch error:', error);
            return Promise.reject(error);
        });
}


function showStreak() {
    fetch('http://127.0.0.1:5000/streak')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            var streak = data;
            var container = $('#streak');
            container.empty();

            var html = '<div class="streaktext" >' + streak + '<i class="fa-solid fa-fire" style="color: #ee7320;"></i></div>';

            container.append(html);
        })
        .catch(error => {
            console.error('Fetch error:', error);
            return Promise.reject(error);
        });
}
