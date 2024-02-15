// script.js
document.addEventListener('DOMContentLoaded', function() {
    // Notları listeleme
    fetchNotlar();

    // Not ekleme formunun dinlenmesi
    document.getElementById('not-ekle-form').addEventListener('submit', function(event) {
        event.preventDefault();
        const baslik = document.getElementById('baslik').value;
        const icerik = document.getElementById('icerik').value;
        ekleNot(baslik, icerik);
    });
});

function fetchNotlar() {
    fetch('/notlar')
        .then(response => response.json())
        .then(notlar => {
            const notlarHTML = notlar.map(not => `<div><h3>${not.baslik}</h3><p>${not.icerik}</p></div>`).join('');
            document.getElementById('notlar').innerHTML = notlarHTML;
        });
}

function ekleNot(baslik, icerik) {
    fetch('/notlar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ baslik, icerik })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        fetchNotlar(); // Notları yeniden listele
    });
}
