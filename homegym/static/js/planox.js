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

            return fetch('http://127.0.0.1:5000/planotreino/'+ planId) 
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
                    var container = $('#content');
                    container.empty();
                    var planDetails = data[0]
                    var exercises = data[1]
                    // inicio do cabeçalho
                    var html = '<div class="maindiv">';
                    html += '<div class="Info">';
                    html += '<div class="IMGcontainer"><img src=../' + planDetails[4] + ' class="meusplanosimg" ></div>';
                    html += '<div class="text"><h3 class="PlanNumber">Plano '+ planNumber +'</h3>';
                    html += '<h3 class="Details">'+planDetails[0]+'</h3></div></div>';
                    html += '<p id="datetime" class="datetime-container"><span class="time"></span><span class="date"></span></p></div></div>';
                    // fim do cabeçalho
                    html += '<div class="description"><p class="d1">Description: </p> ' +'<p>'+ planDetails[1] + '</p></div>';
                    html += '<div class="duration"><p class="dur1">Duration: </p> ' +'<p>'+ planDetails[3] + ' segundos</p></div>';
                    html += '<div class="type"><p class="t1">Type: </p>' + '<p>' + planDetails[2] + '</p></div>';
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

            return fetch('http://127.0.0.1:5000/planotreino/'+ planId) 
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    var container = $('#content');
                    container.empty();

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

function convertToEmbedUrl(url) {
    let videoId = url.split('v=')[1];
    let embedUrl = 'https://www.youtube.com/embed/' + videoId + '?autoplay=1&mute=1&loop=1&playlist=' + videoId;
    return embedUrl;
}



//mostrar stats no final do plano e caso user ganhe badges adquirir a devida badge!
