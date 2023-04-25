const API_URL = "http://localhost:8000";

function createList(items) {
    const ul = document.createElement("ul");
    for (const item of items) {
        const li = document.createElement("li");
        li.textContent = item;
        ul.appendChild(li);
    }
    return ul;
};

async function fetchFilms() {
    const response = await fetch(`${API_URL}/films`);
    if (!response.ok) {
        console.error("Error fetching films:", response.status, response.statusText);
        return;
    }
    const films = await response.json();

    console.log("Fetched films:", films);

    const filmList = document.getElementById("films");

    for (const film of films) {
        const filmDiv = document.createElement("div");
        filmDiv.className = "film";
        filmDiv.innerHTML = `
            <h3>${film.title}</h3>
            <p>Director: ${film.director}</p>
            <p>Year: ${film.year}</p>
            <p>Description: ${film.description}</p>
            <p>Length: ${film.length}</p>
            <p>Rating: ${film.rating}</p>
        `;

        const categories = film.categories.map(category => category.category_name);
        const categoryList = createList(categories);
        filmDiv.appendChild(document.createTextNode("Categories: "));
        filmDiv.appendChild(categoryList);

        const actors = film.cast.map(actor => `${actor.first_name} ${actor.last_name}`);
        const actorList = createList(actors);
        filmDiv.appendChild(document.createTextNode("Actors: "));
        filmDiv.appendChild(actorList);

        const images = film.image.map(image => {
            const img = document.createElement("img");
            img.src = image.image_url;
            img.width = 100;
            return img;
        }
        );
        for (const image of images) {
            filmDiv.appendChild(image);
        }

        filmList.appendChild(filmDiv);
    }
}


fetchFilms();
