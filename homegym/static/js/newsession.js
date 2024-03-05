function onFrameLoad() {
    const iframe = document.getElementById('jitsiFrame');
    const api = iframe.contentWindow.api;

    


    // Automatically join the call
    api.executeCommand('displayName', 'JoseSilva'); // Set your display name
    api.executeCommand('toggleAudio');
    api.executeCommand('toggleVideo');

    api.addEventListener('videoConferenceJoined', () => {
        console.log('Local User Joined');
    });
  }

