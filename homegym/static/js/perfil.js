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

            var html = '<div class="title">Day Streak:' + streak + ' &#128525</div>';
            
            container.append(html);
        })
        .catch(error => {
            console.error('Fetch error:', error);
            return Promise.reject(error);
        });
}

function getProgress(){
    fetch('http://127.0.0.1:5000/progress')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            var container = $('#content');
            container.empty();

            var plansDone = data.plans_done;
            var exsDone = data.exs_done;
            var avgTime = data.avg_time;

            var html = '<div style="margin-top: 50px;">'; 
            html += '<p class="stats2">ESTATÍSTICAS</p>';
            html += '<div class="title">Treinos Feitos: ' + plansDone + '</div>';
            html += '<div class="title">Exercicios Feitos: ' + exsDone + '</div>';
            html += '<div class="title">Tempo Médio de Treino: ' + avgTime + ' s</div></div>';

            container.append(html);
        })
        .catch(error => {
            console.error('Fetch error:', error);
            return Promise.reject(error);
        });
}

function loadHeader(){
    document.getElementById('header').innerHTML = `
        <div class="profile">
            <div class="welcome">
                <div class="container2" style="background-image: url('{{image_path}}');"></div>
                <div class="text">
                    <h1>Bem vindo,</h1>
                    <h2>{{username}}</h2>
                </div>
            </div>
            <p id="datetime" class="datetime-container">
                <span class="time"></span>
                <span class="date"></span>
            </p>
        </div>`;

}

