function showLevel() {
    fetch('http://127.0.0.1:5000/getlevel')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            var container = $('#level');
            container.empty();
            var html = '<div class="leveltext"> Nivel ' + data + ' <i class="fa-solid fa-star" style="color: #FFD43B;"></i></div>';
            container.append(html);
        })
        .catch(error => {
            console.error('Fetch error:', error);
            return Promise.reject(error);
        });
}
