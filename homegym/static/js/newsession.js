
function EnterNewSession(sessionid) {
    
    const domain = 'meet.jit.si';
    const options = {
        roomName: sessionid,
        width: 700,
        height: 700,
        parentNode: document.querySelector('#meet'),
        interfaceConfigOverwrite: { TILE_VIEW_MAX_COLUMNS: 2 }
    };
    
    const api = new JitsiMeetExternalAPI(domain, options);
    api.executeCommand('displayName', 'José');

    
}