function showStreak() {
    fetch('/streak')
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

            var html = '<div class="streak" >Streak ' + streak + ' <img src="../static/img/badge4image.jpeg" alt="Icon" style="width: 20px; height: 20px;"></div>';

            container.append(html);
        })
        .catch(error => {
            console.error('Fetch error:', error);
            return Promise.reject(error);
        });
}

function getBadges() {
    Promise.all([
        fetch('/userBadges'),
        fetch('/allBadges')
    ])
        .then(async ([res1, res2]) => {
            if (!res1.ok) {
                throw new Error(`HTTP error! Status: ${res1.status}`);
            }
            if (!res2.ok) {
                throw new Error(`HTTP error! Status: ${res2.status}`);
            }
            return Promise.all([res1.json(), res2.json()]);
        })
        .then(([userBadges, allBadges]) => {
            console.log(userBadges, allBadges);
            var container = $('#content');
            container.empty();
        
            var html = '<p class="stats2">SUAS CONQUISTAS</p>';
            html += '<div class="card-container">'; 

            for (badge of userBadges) {
                html += '<div class="card">';
                html += '<img src="' + badge[3] + '" alt="Avatar" style="width:100%;">';
                html += '<div class="container">'
                html += '<div class="text-stats">' + badge[0] + ' </div>';
                html += '<div class="text-stats">' + badge[1] + ' </div>';
                html += '</div>';
                html += '</div>';

            }
            html += '</div>';

            var badgesToWin = allBadges.filter(badge => !userBadges.some(userBadge => userBadge[0] === badge[0]));

            // Display the badges that the user doesn't have yet
            html += '<p class="stats2">CONQUISTAS POR GANHAR</p>';
            html += '<div class="card-container">';

            for (badge of badgesToWin) {
                html += '<div class="card">';
                html += '<img src="' + badge[3] + '" alt="Avatar" style="width:100%; filter: grayscale(100%);">';
                html += '<div class="container">'
                html += '<div class="text-stats">' + badge[0] + ' </div>';
                html += '<div class="text-stats">' + badge[1] + ' </div>';
                html += '</div>';
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

function showinfo() {
    ```<div class="left-side">
            <div class="height-weight">
                <div class="stat height">{{height}} cm</div>
                <div class="stat weight">{{weight}} kg</div>
            </div>
            <div class="conquistas">Conquistas do mês</div>
            <div class="achievements-container">
                {% for badge_image in badge_images %}
                    <div class="achievement" style="background-image: url('{{badge_image}}');"></div>
                {% endfor %}
            </div>
            <div class="casa-viva">Projeto CasaViva+</div>
            <div class="privacidade">Politicas de privacidade</div>
            <div class="definicoes">Definições</div>
        </div>
        
        ir buscar measurements a base de dados```
}

function getProgress() {
    return fetch('/progress')
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
            var total_time = data.total_time;

            var html = '<div class="stats2">';
            html += '<div class="titleprg">Total de tempo a treinar</div>';
            html += '<div class="title_group1"> <div class="titlevalues_animated_1">' + total_time + '</div><span id="timedesign">min</span></div>';
            html += '<div class="titleprg">Planos de treino realizados</div>';
            html += '<div class="titlevalues">' + plansDone + '</div>';
            html += '<div class="titleprg">Tempo médio por treino</div>';
            html += '<div class="title_group1"> <div class="titlevalues_animated_2">' + avgTime + '</div> <span id="timedesign">seg</span></div></div>';

            html += `<div id="progress-bar">
                        <div id="progress"></div>
                    </div>
                    <div id="level-indicators">
                        <span id="current-level"></span>
                        <span id="next-level"></span>
                    </div>`;

            container.append(html);


            animateNumber($('.titlevalues_animated_1'), total_time);
            animateNumber($('.titlevalues'), plansDone);
            animateNumber($('.titlevalues_animated_2'), avgTime);

            function animateNumber(element, newValue) {
                $({ value: 0 }).animate({ value: newValue }, {
                    duration: 1000,
                    easing: 'swing',
                    step: function () {

                        var formattedValue = this.value;
                        if (element.hasClass('titlevalues_animated_1')) {
                            formattedValue = this.value.toFixed(2);
                        } else if (element.hasClass('titlevalues_animated_2')) {
                            formattedValue = this.value.toFixed(0);
                        }
                        else {
                            formattedValue = this.value.toFixed(0);
                        }
                        element.text(formattedValue);
                    }
                });
            }

        })
        .catch(error => {
            console.error('Fetch error:', error);
            return Promise.reject(error);
        });
}

function showLevelProgress() {
    return fetch('/getlevelprogress')
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

            document.getElementById('current-level').textContent = `NÍVEL ${current_level[0]}`;
            document.getElementById('next-level').textContent = `NÍVEL ${next_level[0]}`;


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

