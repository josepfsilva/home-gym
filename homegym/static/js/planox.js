function getPlanNumber() {
    let url = new URL(window.location.href);
    let pathSegments = url.pathname.split('/');
    // Get the plan number
    let planNumber = parseInt(pathSegments[pathSegments.length - 1].replace(/\D/g, ''));
    return planNumber;
}

function headPlan(){
    checkIfPlanExists(planNumber).then(exists => {
        if (exists) {
            console.log(planNumber)
            LoadPlanHead(planNumber);
        }
    });
}

function LoadPlanHead(planNumber) {
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

            return fetch('http://127.0.0.1:5000/planotreino/'+ planId) 
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    // Process the data and update the HTML content
                    console.log(data);
                    //document.getElementById('content').innerText = data.message;
                    var container = $('#content');
                    container.empty();
                    var planDetails = data[0]
                    var html = '<div> <h1>Plano '+ planNumber + ' - ' + planDetails[0] + '</h1></div>';
                    
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

            fetch('http://127.0.0.1:5000/planotreino/'+ planId) 
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    // Process the data and update the HTML content
                    console.log(data);
                    //document.getElementById('content').innerText = data.message;
                    var container = $('#content');
                    container.empty();
                    var planDetails = data[0]
                    var exercises = data[1]
                    var html = '<div>';
                    html += '<h3>Plano '+ planNumber + ' : ' + planDetails[0] + '</h3>';
                    html += '<p>Description: ' + planDetails[1] + '</p>';
                    html += '<p>Type: ' + planDetails[2] + '</p>';
                    html += '</div> <h3>Exercises</h3>';
                    html += '<div class="menu"> ';  
                    for (var exerciseId in exercises) {
                        var exerciseDetails = exercises[exerciseId];
                        html += '<div class="container"> <div class="content"> <h3>'+ exerciseDetails[0]+'</h3> <p>'+ exerciseDetails[1] +'</p> <p>'+ exerciseDetails[3] +'</p> <p>'+ exerciseDetails[4] +'</p> </div> </div>'
                    }
                    
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


function loadExercise(planNumber,count) {
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

            return fetch('http://127.0.0.1:5000/planotreino/'+ planId) 
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
                    console.log(exercises)
                    
                    var exerciseDetails = exercises[count];

                    let videoFrame = document.getElementById('videoFrame');
                    videoFrame.src = ""; 
                    videoFrame.src = convertToEmbedUrl(exerciseDetails[2]);

                    var html = '<div class="container3"> <div class="content"> <h3>'+ exerciseDetails[0]+'</h3> <p>'+ exerciseDetails[1] +'</p> <p>'+ exerciseDetails[3] +'</p> <p>'+ exerciseDetails[4] +'</p> </div> </div>'
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

function runForTime(seconds) {
    return new Promise(resolve => {
        let timerElement = document.getElementById('timer');
        let timeLeft = seconds;
        timerElement.textContent = timeLeft;

        setTimeout(() => {
            clearInterval(intervalId);  // Stop the timer after the specified number of seconds
            resolve();
        }, seconds * 1000);

        let intervalId = setInterval(() => {
            timeLeft--;  // Decrease the time left by 1
            timerElement.textContent = timeLeft;  // Update the timer on the screen
        }, 1000); 
    });
}

function convertToEmbedUrl(url) {
    let videoId = url.split('v=')[1];
    let embedUrl = 'https://www.youtube.com/embed/' + videoId + '?autoplay=1&mute=1&loop=1&playlist=' + videoId;
    return embedUrl;
}



//mostrar stats no final do plano e caso user ganhe badges adquirir a devida badge!
