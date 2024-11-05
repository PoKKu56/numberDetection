//main.html
const uploadBox = document.getElementById('uploadBox');
const fileInput = document.getElementById('fileInput');

uploadBox.addEventListener('click', () => {
    fileInput.click();
});

uploadBox.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadBox.classList.add('drag-over');
});

uploadBox.addEventListener('dragleave', () => {
    uploadBox.classList.remove('drag-over');
});

uploadBox.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadBox.classList.remove('drag-over');
    const files = e.dataTransfer.files;
    if (files.length) {
        fileInput.files = files;
        const event = new Event('change');
        fileInput.dispatchEvent(event);
    }
});

fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (file) {
        console.log('Загружен файл:', file.name);
    }
});

// devs.html
document.addEventListener("DOMContentLoaded", function() {
    const readmeUrl = 'https://raw.githubusercontent.com/PoKKu56/numberDetection/main/README.md';
    fetch(readmeUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Сеть ответила с ошибкой: ' + response.status);
            }
            return response.text();
        })
        .then(markdown => {
            const htmlContent = marked(markdown);
            const contentContainer = document.getElementById("readme-content");
            contentContainer.innerHTML = htmlContent;
        })
        .catch(error => console.error('Ошибка загрузки README.md:', error));
});
