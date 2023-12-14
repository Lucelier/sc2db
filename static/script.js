$(document).ready(function () {
    addRandomDots();
});

function addRandomDots() {
    const headers = document.querySelectorAll("#result-table th");

    headers.forEach(header => {
        const numberOfDots = getRandomInt(3, 6); // Anzahl der Punkte zwischen 3 und 6
        const dotSize = 12; // Größe der Punkte

        for (let i = 0; i < numberOfDots; i++) {
            const dot = document.createElement("span");
            dot.className = "dot";
            dot.innerHTML = "•";
            dot.style.fontSize = `${dotSize}px`;
            dot.style.position = "absolute";
            dot.style.top = `${getRandomInt(10, 80)}%`; // Zufällige vertikale Position
            dot.style.left = `${getRandomInt(10, 90)}%`; // Zufällige horizontale Position
            header.appendChild(dot);
        }
    });
}

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
