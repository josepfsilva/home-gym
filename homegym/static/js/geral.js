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
            var html = '<div class="leveltext"> Nivel ' + level + ' <img src="../static/img/star.png" alt="Icon" style="width: 20px; height: 20px;"></div>';
            container.append(html);

            if(leveledUp==1){
                Swal.fire({
                    title: 'Parabéns!',
                    text: 'Subiu para o Nivel '+ level + '',
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


function showStreak(){
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

            var html = '<div class="streaktext" >'+ streak +' <img src="../static/img/badge4image.jpeg" alt="Icon" style="width: 20px; height: 20px;"></div>';
            
            container.append(html);
        })
        .catch(error => {
            console.error('Fetch error:', error);
            return Promise.reject(error);
        });
}
