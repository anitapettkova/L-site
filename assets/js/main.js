document.addEventListener("DOMContentLoaded", () => {
    // 1. Automatic Nav Link Active State
    const currentPath = window.location.pathname.replace(/index\.html$/, "");
    const navLinks = document.querySelectorAll("nav a");

    navLinks.forEach(link => {
        const linkPath = link.getAttribute("href").replace(/index\.html$/, "");
        link.classList.remove("active");

        if (linkPath === currentPath || (linkPath !== "/" && currentPath.startsWith(linkPath))) {
            link.classList.add("active");
        }
    });

    // 2. Footer Clock
    function updateClock() {
        const clockEl = document.getElementById('sys-time');
        if (clockEl) {
            const now = new Date();
            clockEl.textContent = `SYS_TIME: ${now.toLocaleTimeString('en-US', { hour12: false })}`;
        }
    }
    setInterval(updateClock, 1000);
    updateClock();
});
