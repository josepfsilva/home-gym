function getPlanNumber() {
    let url = new URL(window.location.href);
    let pathSegments = url.pathname.split('/');
    // Get the plan number
    let planNumber = parseInt(pathSegments[pathSegments.length - 1].replace(/\D/g, ''));
    return planNumber;
}

function getPlanId(planNumber) { // tried to use in other functions but it was not working
    return fetch('http://127.0.0.1:5000/planosOrder')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            return data[planNumber];
        })
        .catch(error => {
            console.error('Fetch error:', error);
            return Promise.reject(error);
        });
}

function loadPlanHead(planNumber) {
    return fetch('http://127.0.0.1:5000/planosOrder')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Process the data and update the HTML content
            let planId = data[planNumber];                 //id real na db

            return fetch('http://127.0.0.1:5000/planotreino/' + planId)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    var container = $('#content');
                    container.empty();
                    var planDetails = data[0]
                    var html = '<div class="planhead"> <p>Plano ' + planNumber + ' - ' + planDetails[0] + '<p></div>';

                    container.append(html);
                })
                .catch(error => {
                    console.error('Fetch error:', error);
                });

        })
        .catch(error => {
            console.error('Fetch error:', error);
        });

}

function loadPlanInfo(planNumber) {
    fetch('http://127.0.0.1:5000/planosOrder')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Process the data and update the HTML content
            let planId = data[planNumber];

            fetch('http://127.0.0.1:5000/planotreino/' + planId)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {

                    var mmiCli_1 = null;
                    mmiCli_1 = new MMIClient(null, "https://" + host + ":8000/IM/USER1/APPSPEECH");
                    sendToVoice("Plano " + planNumber);
                    function sendToVoice(texto) {
                        //let speak = "&lt;speak version=\"1.0\" xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.w3.org/2001/10/synthesis http://www.w3.org/TR/speech-synthesis/synthesis.xsd\" xml:lang=\"pt-PT\"&gt;&lt;p&gt;" + "quadrado" + "&lt;/p&gt;&lt;/speak&gt";
                        let speak = "<speak version=\"1.0\" xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.w3.org/2001/10/synthesis http://www.w3.org/TR/speech-synthesis/synthesis.xsd\" xml:lang=\"pt-PT\"><p>" + texto + "</p></speak>";
                        var result = speak;
                        mmiCli_1.sendToIM(new LifeCycleEvent("APPSPEECH", "IM", "text-1", "ctx-1").
                            doStartRequest(new EMMA("text-", "text", "command", 1, 0).
                                setValue(JSON.stringify(result))));
                    }
                    var container = $('#content');
                    container.empty();
                    var planDetails = data[0]
                    var exercises = data[1]
                    console.log(exercises);
                    // inicio do cabeçalho
                    var html = '<div class="maindiv">';
                    html += '<div class="Info">';
                    html += '<div class="IMGcontainer"><img src=../' + planDetails[4] + ' class="meusplanosimg" ></div>';
                    html += '<div class="text">'
                    html += '<p>Treino de</p>';
                    html += '<h3>' + planDetails[0] + '</h3>';
                    html += '<div class="horizontal-line"></div>';
                    html += '<h3 class="PlanNumber">Plano ' + planNumber + '</h3></div>';
                    html += '<p id="datetime" class="datetime-container"><span class="time"></span><span class="date"></span></p></div></div>';
                    // fim do cabeçalho
                    //inicio dos detalhes
                    html += '<div class="details"><div class="TypeandTime"><div class="duration"><p class="subtitle">Duration: </p> ' + '<p>' + planDetails[3] + ' segundos</p></div>';
                    html += '<div class="type"><p class="subtitle">Type: </p>' + '<p>' + planDetails[2] + '</p></div></div>';
                    html += '<div class="description">' + '<p>' + planDetails[1] + '</p></div></div>';
                    //fim dos detalhes
                    //Exercicios
                    html += '</div> <div class="ContentEX"><h3 class="Exercicios">Exercícios:</h3>';
                    html += '<div class="menu"> ';
                    for (var exerciseId in exercises) {
                        var exerciseDetails = exercises[exerciseId];
                        html += '<div class="ExContainer"><div class="ExImage"><img src=../' + exerciseDetails[5] + '> <h3 class="ExName">' + exerciseDetails[0] + '</h3></div ><div class="lowContent"><div class="type"><p class="ExType">Tipo: </p><p>' + exerciseDetails[3] + '</p></div> <div class="Diff"> <p class="ExType">Dificuldade: </p><p>' + exerciseDetails[4] + '</p></div></div ></div > '
                        console.log('../' + exerciseDetails[2]);
                        //html += 'div class="ExImage"><img src=../' + exerciseDetails[] + ' class="Eximg" ></div>';
                    }
                    html += '</div></div>';
                    //fim dos exercicios
                    html += '<button class="button"><svg xmlns="http://www.w3.org/2000/svg" width="24" viewBox="0 0 24 24" height="24" fill="none" class="svg-icon"><g stroke-width="2" stroke-linecap="round" stroke="#ffffff"><rect y="3" x="9" width="6" rx="3" height="11"></rect><path d="m12 18v3"></path><path d="m8 21h8"></path><path d="m19 11c0 3.866-3.134 7-7 7-3.86599 0-7-3.134-7-7"></path></g></svg><span class="lable">Iniciar</span></button > '

                    container.append(html);
                })
                .catch(error => {
                    console.error('Fetch error:', error);
                });

        })
        .catch(error => {
            console.error('Fetch error:', error);
        });

}


function loadExercise(planNumber, count) {
    return fetch('http://127.0.0.1:5000/planosOrder')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Process the data and update the HTML content
            let planId = data[planNumber];

            return fetch('http://127.0.0.1:5000/planotreino/' + planId)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    // Process the data and update the HTML content
                    //document.getElementById('content').innerText = data.message;
                    var container = $('#exercise');
                    container.empty();
                    var exercises = data[1]
                    var totalExercises = exercises.length; // Get the total number of exercises

                    var exerciseDetails = exercises[count];


                    let videoFrame = document.getElementById('videoFrame');
                    videoFrame.src = "";
                    videoFrame.src = convertToEmbedUrl(exerciseDetails[2]);

                    var html = `<div class="videoContainer">
                                    <div class="content">
                                        <h3 >${exerciseDetails[0]}</h3>
                                        <span id="word">Exercício:</span> <span id="counter">${count + 1}/${totalExercises}</span>
                                        <p id = "descricao"> ${exerciseDetails[1]} </p>
                                        <div id="conquistas-container">
                                            <p class = "conquistas"> Conquistas: </p>
                                            <div class="badges-gained"></div>
                                            <div class="badges-gained"></div>
                                            <p id = "conquistas-next"> Próximas conquistas: </p>
                                            <div class="badges-next"></div>
                                            <div class="badges-next"></div>
                                        </div>
                                    </div>
                                </div>`;
                    container.append(html);
                })
                .catch(error => {
                    console.error('Fetch error:', error);
                });

        })
        .catch(error => {
            console.error('Fetch error:', error);
        });

}

function getPlanDuration(planNumber) {
    return fetch('http://127.0.0.1:5000/planosOrder')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Process the data and update the HTML content
            let planId = data[planNumber];                 //id real na db

            return fetch('http://127.0.0.1:5000/planotreino/' + planId)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    var planDetails = data[0];
                    return planDetails[3];
                })
                .catch(error => {
                    console.error('Fetch error:', error);
                });

        })
        .catch(error => {
            console.error('Fetch error:', error);
        });

}

function sendFinishPlan(elapsedTime, planNumber) {
    let data = {
        planNumber: planNumber,
        elapsedTime: elapsedTime,
    };

    // Make a POST request to the Flask route
    return fetch('http://127.0.0.1:5000/FinishPlan', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data) // Convert the data to a JSON string
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch((error) => {
        console.error('Error:', error);
    });
}


function formatTime(timeInMilliseconds) {
    let seconds = Math.floor((timeInMilliseconds / 1000) % 60);
    let minutes = Math.floor((timeInMilliseconds / (1000 * 60)) % 60);
    let hours = Math.floor((timeInMilliseconds / (1000 * 60 * 60)) % 24);

    hours = (hours < 10) ? "0" + hours : hours;
    minutes = (minutes < 10) ? "0" + minutes : minutes;
    seconds = (seconds < 10) ? "0" + seconds : seconds;

    return hours + ":" + minutes + ":" + seconds;
}

function convertToEmbedUrl(url) {
    let videoId = url.split('v=')[1];
    let embedUrl = 'https://www.youtube.com/embed/' + videoId + '?autoplay=1&mute=1&loop=1&playlist=' + videoId;
    return embedUrl;
}



//mostrar stats no final do plano e caso user ganhe badges adquirir a devida badge!