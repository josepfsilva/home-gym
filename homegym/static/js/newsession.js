function  enterNewSession(sessionname) {
    const domain = 'meet.jit.si';
    const options = {
        roomName: sessionname,
        width: 700,
        height: 700,
        parentNode: document.querySelector('#meet'),
        lang: 'pt',
        configOverwrite: { prejoinPageEnabled: false},
    };
    
    const api = new JitsiMeetExternalAPI(domain, options);
  }

