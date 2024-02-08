function loadPlans() {
    fetch('http://127.0.0.1:5000/planos') 
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => { 
                    console.log(data);
                    // Process the data and update the HTML content
                    var container = $('#content');
                    container.empty();

                    plans = data[0];
                    order = data[1];
                    var html='<div class="menu"> '
                    for (var planId in plans) {
                        var planDetails = plans[planId];
                        var planOrder = order[planId];

                        html += '<div class="container"> <div class="content"> <h3>'+ planDetails[0]+'</h3> <p> Plano '+ planOrder +' </p></div> </div>'
                        
                    }
                    html += '</div>'
                    container.append(html);
                    container.removeClass('loaded').addClass('loaded');
                })
                .catch(error => {
                    console.error('Fetch error:', error);
                });
            }

function PlanIdOrder(planNumber){ // returns planid using order
    fetch('http://127.0.0.1:5000/planosOrder')
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
                    html += '<h3>Name: ' + planDetails[0] + '</h3>';
                    html += '<p>Description: ' + planDetails[1] + '</p>';
                    html += '<p>Type: ' + planDetails[2] + '</p>';
                    html += '</div> <h3>Exercises</h3>';
                    html += '<div class="menu"> ';  
                    for (var exerciseId in exercises) {
                        var exerciseDetails = exercises[exerciseId];
                        html += '<div class="container"> <div class="content"> <h3>'+ exerciseDetails[0]+'</h3> <p>'+ exerciseDetails[1] +'</p> <p>'+ exerciseDetails[2] +'</p> <p>'+ exerciseDetails[3] +'</p> </div> </div>'
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

function checkIfPlanExists(PlanN){
    return fetch('http://127.0.0.1:5000/planosOrder')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            return data[PlanN] != undefined;
        })
        .catch(error => {
            console.error('Fetch error:', error);
            return false;
        });
}

function loadContent(htmlFilePath) { //not used
        
    var xhr = new XMLHttpRequest();
    xhr.open('GET', htmlFilePath, true);

    xhr.onload = function () {
        if (xhr.status >= 200 && xhr.status < 300) {
            document.getElementById('content').innerHTML = xhr.responseText;
        } else {
            console.error('Failed to load content');
        }
    };

    xhr.onerror = function () {
        console.error('Network error occurred');
    };

    xhr.send();

}       


function sendToVoice(texto){
    //let speak = "&lt;speak version=\"1.0\" xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.w3.org/2001/10/synthesis http://www.w3.org/TR/speech-synthesis/synthesis.xsd\" xml:lang=\"pt-PT\"&gt;&lt;p&gt;" + "quadrado" + "&lt;/p&gt;&lt;/speak&gt";
  let speak = "<speak version=\"1.0\" xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.w3.org/2001/10/synthesis http://www.w3.org/TR/speech-synthesis/synthesis.xsd\" xml:lang=\"pt-PT\"><p>"+texto+"</p></speak>";
  var result = speak;
      mmiCli_1.sendToIM(new LifeCycleEvent("APPSPEECH", "IM", "text-1", "ctx-1").
          doStartRequest(new EMMA("text-", "text", "command", 1, 0).
            setValue(JSON.stringify(result))));
  }