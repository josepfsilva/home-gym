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

            var html = '<div class="streak" >Streak '+ streak +' <img src="../static/img/badge4image.jpeg" alt="Icon" style="width: 20px; height: 20px;"></div>';
            
            container.append(html);
        })
        .catch(error => {
            console.error('Fetch error:', error);
            return Promise.reject(error);
        });
}

function getBadges(){
    fetch('http://127.0.0.1:5000/allBadges')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            var container = $('#content');
            container.empty();
        
            var html = '<p class="stats2">SUAS CONQUISTAS</p>' + '<div class="achievements-container2">';
            
            for (badge of data) {
                html += '<div class="badge-container">';
                html += '<div class="text-stats">"' + badge[0] + ' "</div>';
                html += '<div class="achievement" style="background-image: url(' + badge[3] + ');"></div>';
                html += '</div>';

            }
            html += '</div>';
            container.append(html);
        })
        .catch(error => {
            console.error('Fetch error:', error);
            return Promise.reject(error);
    });
}

function getProgress(){
    return fetch('http://127.0.0.1:5000/progress')
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

            var html = '<div class="stats2">PROGRESSO';
            html += '<div class="titleprg">Treinos Feitos: ' + plansDone + '</div>';
            html += '<div class="titleprg">Exercicios Feitos: ' + exsDone + '</div>';
            html += '<div class="titleprg">Tempo Médio de Treino: ' + avgTime + ' s</div></div>';

            html += `<div id="progress-bar">
                        <div id="progress"></div>
                    </div>
                    <div id="level-indicators">
                        <span id="current-level"></span>
                        <span id="next-level"></span>
                    </div>`;

            container.append(html);
        })
        .catch(error => {
            console.error('Fetch error:', error);
            return Promise.reject(error);
        });
}

function showLevelProgress(){
    return fetch('http://127.0.0.1:5000/getlevelprogress')
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        console.log(data)
        var user_xp = data.user_xp;
        var current_level = data.current_level;
        var next_level = data.next_level;

        var levelpercentage = (user_xp / next_level[1]) * 100;
        setProgress(levelpercentage);

        document.getElementById('current-level').textContent = `NIVEL ${current_level[0]}`;
        document.getElementById('next-level').textContent = `NIVEL ${next_level[0]}`;

        
    })
    .catch(error => {
        console.error('Fetch error:', error);
        return Promise.reject(error);
    });
}

function setProgress(percentage) {
    var progressBar = document.getElementById('progress');
    progressBar.style.width = percentage + '%';
    console.log(percentage);
  }
