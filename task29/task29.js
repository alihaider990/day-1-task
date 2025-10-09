class   Movieratingdashboard {
    constructor() {
        this.movies = [];
    }

    addmovie(title, genre) {
        const movie = {
            id: this.movies.length + 1,
            title: title,
            genre: genre,
            ratings: []
        };
        this.movies.push(movie);
    }
    getAverageRating(movieId) {
        const movie = this.movies.find(m => m.id === movieId);
        if (!movie || movie.ratings.length === 0) return 0;
        const sum = movie.ratings.reduce((a, b) => a + b, 0);
        return +(sum / movie.ratings.length).toFixed(1);
    }

    addrating(movieId, rating) {
        const movie = this.movies.find(m => m.id === movieId);
        if (movie) {
            movie.ratings.push(rating);
            const sum = movie.ratings.reduce((a,b) => a+b,0);
            const avg = sum/movie.ratings.length;
            movie.avgRating = +(sum/movie.ratings.length).toFixed(1);
        }
    }
}

const movies = new Movieratingdashboard();

movies.addmovie("batman", "Action");
movies.addmovie("spider man", "Action");
movies.addmovie("spencer confidential", "Action");
movies.addmovie("fast and furious", "Action");
movies.addmovie("formula 1", "racing");
movies.addmovie("the karate kid", "Action");
movies.addmovie("commondo  ", "Action");
movies.addmovie("saiyaara", "romance");
movies.addmovie("tiger zinda hai", "Action");
movies.addmovie("sultan", "Action");

movies.addrating(1, 5);
movies.addrating(1, 4);
movies.addrating(2, 5);
movies.addrating(2, 4);
movies.addrating(3, 5);
movies.addrating(3, 3);
movies.addrating(4, 5);
movies.addrating(4, 2);
movies.addrating(5, 5);
movies.addrating(5, 3);
movies.addrating(6, 5);
movies.addrating(6, 1);

function display_movie_details() {
    const ratedMovies = movies.movies
        .filter(movie => movie.ratings.length > 0)
        .map(movie => {
            const avg = movie.ratings.reduce((sum, r) => sum + r, 0) / movie.ratings.length;
            return { ...movie, avgRating: parseFloat(avg.toFixed(1)) };
        });

    const top3 = [...ratedMovies].sort((a, b) => b.avgRating - a.avgRating).slice(0, 3);
    const lowestRated = [...ratedMovies].sort((a, b) => a.avgRating - b.avgRating)[0];

    const genrecount = {};
    for (let movie of ratedMovies) {
        genrecount[movie.genre] = (genrecount[movie.genre] || 0) + 1;
    }
    

    let commongenere = null;
    let maxcount = 0;
    
    for(let genre in genrecount){
        if(genrecount[genre] > maxcount){
            maxcount = genrecount[genre];
            commongenere = genre;
        }
    }

    console.log("\n🎬 Top 3 Movies by Rating:");
    top3.forEach((movie, i) => console.log(`${i + 1}. ${movie.title} (${movie.avgRating})`));
    
    console.log(`\n  Lowest Rated Movie: ${lowestRated.title} (${lowestRated.avgRating})`);
    console.log(`\n  Most Common Genre: ${commongenere}`);
}

console.table(movies.movies);

display_movie_details();





