(async function universityCourses() {
    try {
        const res = await fetch("https://jsonplaceholder.typicode.com/posts");
        if (!res.ok) throw new Error("Failed to fetch data");

        const rawData = await res.json();
        const categories = ["AI", "ML", "Neural Network", "React"];

        const courses = rawData.slice(0, 20).map((item, i) => ({
            id: item.id,
            title: item.title,
            summary: item.body,
            category: categories[i % categories.length],
            enrolled: 80 + Math.floor(Math.random() * 150),
            rating: +(3 + Math.random() * 2).toFixed(1) 
        }));

        const grouped = {};
        for (const course of courses) {
            if (!grouped[course.category]) grouped[course.category] = [];
            grouped[course.category].push(course);
        }

        const topCourses = [...courses].sort((a, b) => b.rating - a.rating).slice(0, 3);

        function enroll(courseId, count = 1) {
            const course = courses.find(c => c.id === courseId);
            if (course) course.enrolled += count;
        }

        const categoryrating = [];
        for (const category in grouped) {
            let total = 0;
            for (const course of grouped[category]) {
                total += course.enrolled;
            }
            categoryrating.push({ category: category, totalEnrollments: total });
        }
        categoryrating.sort((a, b) => b.totalEnrollments - a.totalEnrollments);

        const lowRatingCourses = courses.filter(c => c.rating < 4);

        
        console.log("Loaded", courses.length, "courses.");
        
        console.log("\nTop 3 Courses by Rating:");
        topCourses.forEach((course, index) => {
            console.log(`${index + 1}. ${course.title} (Rating: ${course.rating})`);
        });

        console.log("\nMost enrolled category:", categoryrating[0]?.category || "None");

        console.log("\nCourses with rating < 4:");
        lowRatingCourses.forEach(c => console.log("-", c.title, `(Rating: ${c.rating})`));
        
        enroll(1, 3);

    } catch (err) {
        console.error("Error:", err.message);
    }
})();