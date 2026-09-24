document.addEventListener("DOMContentLoaded", () => {
    const navUl = document.querySelector("nav ul");
    if (!navUl) return;

    const currentPath = window.location.pathname;
    const norm = (p) => p.replace(/index\.html$/, "").replace(/\/$/, "");
    const normalizedCurrent = norm(currentPath);

    navUl.querySelectorAll("a").forEach(a => a.classList.remove("active"));

    let exactLink = Array.from(navUl.querySelectorAll("a")).find(a => norm(a.getAttribute("href")) === normalizedCurrent);

    if (exactLink) {
        exactLink.classList.add("active");
    } else {
        const segments = currentPath.split("/").filter(Boolean);

        if (segments[0] === "blog") {
            
            if (segments.length >= 2) {
                const categorySlug = segments[1];
                const categoryPath = `/blog/${categorySlug}/`;

                let catLink = Array.from(navUl.querySelectorAll("a")).find(a => norm(a.getAttribute("href")) === norm(categoryPath));

                if (!catLink) {
                    const catName = categorySlug
                        .replace(/-/g, " ")
                        .replace(/\b\w/g, l => l.toUpperCase());

                    const li = document.createElement("li");
                    catLink = document.createElement("a");
                    catLink.href = categoryPath;
                    catLink.textContent = catName;
                    li.appendChild(catLink);
                    navUl.appendChild(li);
                }

                if (segments.length === 2) {
                    catLink.classList.add("active");
                } 
                
                else if (segments.length >= 3) {
                    let articleLink = Array.from(navUl.querySelectorAll("a")).find(a => norm(a.getAttribute("href")) === normalizedCurrent);

                    if (!articleLink) {
                        const h1 = document.querySelector("article h1, main h1, h1");
                        let titleText = h1 ? h1.textContent.trim() : "";
                        if (!titleText && document.title) {
                            titleText = document.title.split("|")[0].trim();
                        }
                        if (!titleText) {
                            titleText = segments[2].replace(/\.html$/, "").replace(/-/g, " ");
                        }

                        const displayTitle = titleText.length > 22 
                            ? titleText.substring(0, 19) + "..." 
                            : titleText;

                        const li = document.createElement("li");
                        articleLink = document.createElement("a");
                        articleLink.href = currentPath;
                        articleLink.textContent = displayTitle;
                        articleLink.title = titleText;
                        li.appendChild(articleLink);
                        navUl.appendChild(li);
                    }

                    articleLink.classList.add("active");
                }
            }
        }
    }

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
