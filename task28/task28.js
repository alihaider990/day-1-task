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

        const categorySummary = Object.entries(
            courses.reduce((acc, course) => {
                acc[course.category] = (acc[course.category] || 0) + course.enrolled;
                return acc;
            }, {})
        ).map(([category, totalEnrollments]) => ({ category, totalEnrollments }))
         .sort((a, b) => b.totalEnrollments - a.totalEnrollments);

        
        function enroll(courseId, count = 1) {
            const course = courses.find(c => c.id === courseId);
            if (!course) {
                console.warn(`Course ID ${courseId} not found.`);
                return;
            }
            course.enrolled += count;
            console.log(`${course.title} new enrollment count: ${course.enrolled}`);
        }

        
        const getTopCourses = (n = 3) => [...courses].sort((a, b) => b.rating - a.rating).slice(0, n);
        const getLowRatingCourses = () => courses.filter(c => c.rating < 4);
        const getMostEnrolledCategory = () => categorySummary[0]?.category || "None";

        const topCourses = getTopCourses();
        const lowRatingCourses = getLowRatingCourses();
        const mostEnrolledCategory = getMostEnrolledCategory();

        
        console.log(` Loaded ${courses.length} courses.\n`);
        
        console.log(" Top 3 Courses by Rating:");
        console.table(topCourses.map((c, i) => ({ 
            Rank: i + 1,
            Title: c.title.substring(0, 40), 
            Rating: c.rating, 
            Enrolled: c.enrolled 
        })));

        console.log(`\n Most enrolled category: ${mostEnrolledCategory}`);
        console.log("\n Category Enrollment Summary:");
        console.table(categorySummary);

        console.log(`\n  Courses with rating < 4 (${lowRatingCourses.length} found):`);
        if (lowRatingCourses.length > 0) {
            console.table(lowRatingCourses.map(c => ({ 
                Title: c.title.substring(0, 40), 
                Rating: c.rating,
                Category: c.category
            })));
        }
        
        console.table(courses);

    } catch (err) {
        console.error(" Error:", err.message);
    }
})();