function loadPlans() {
    fetch('http://127.0.0.1:5000/planos') 
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    // Process the data and update the HTML content
                    var container = $('#content');
                    container.empty();
                    var html='<div class="menu"> '
                    for (var planId in data) {
                        var planDetails = data[planId];
                        html += '<div class="container"> <div class="content"> <h3>'+ planDetails[1]+'</h3> <p>'+ planDetails[2]+'</p> <p> Plano 1 </p></div> </div>'
                        
                    }
                    html += '</div>'
                    container.append(html);
                })
                .catch(error => {
                    console.error('Fetch error:', error);
                });
            }

  function loadPlanInfo(planNumber) {
    fetch('http://127.0.0.1:5000/planotreino/'+planNumber) 
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
                    var planDetails = data
                    var html = '<div>';
                    html += '<h3>Name: ' + planDetails[0] + '</h3>';
                    html += '<p>Description: ' + planDetails[1] + '</p>';
                    html += '<p>Type: ' + planDetails[2] + '</p>';
                    html += '</div>';
                    
                    container.append(html);
                })
                .catch(error => {
                    console.error('Fetch error:', error);
                });
  }



function sendToVoice(texto){
    //let speak = "&lt;speak version=\"1.0\" xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.w3.org/2001/10/synthesis http://www.w3.org/TR/speech-synthesis/synthesis.xsd\" xml:lang=\"pt-PT\"&gt;&lt;p&gt;" + "quadrado" + "&lt;/p&gt;&lt;/speak&gt";
  let speak = "<speak version=\"1.0\" xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.w3.org/2001/10/synthesis http://www.w3.org/TR/speech-synthesis/synthesis.xsd\" xml:lang=\"pt-PT\"><p>"+texto+"</p></speak>";
  var result = speak;
      mmiCli_1.sendToIM(new LifeCycleEvent("APPSPEECH", "IM", "text-1", "ctx-1").
          doStartRequest(new EMMA("text-", "text", "command", 1, 0).
            setValue(JSON.stringify(result))));
  }