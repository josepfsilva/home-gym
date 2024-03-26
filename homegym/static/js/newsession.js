
function getSessionName() {
    let url = new URL(window.location.href);
    let pathSegments = url.pathname.split('/');
    // Get the session name
    let sessionname  = pathSegments[pathSegments.length - 1].toLowerCase();
    return sessionname;
}




