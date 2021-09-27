function toggle(section) {
    let x = document.getElementById(section);
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }

}

// Activate SimpleLightbox plugin for portfolio items
new SimpleLightbox({
    elements: '#project a.project-box'
});
