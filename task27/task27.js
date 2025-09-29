(async () => {
    console.log("posting authors...");

    try {
        const postsResponse = await fetch("https://jsonplaceholder.typicode.com/posts");
        const usersResponse = await fetch("https://jsonplaceholder.typicode.com/users");

        if (!postsResponse.ok || !usersResponse.ok) {
            console.log("Couldn't fetch everything properly.");
            return;
        }

        const posts = await postsResponse.json();
        const users = await usersResponse.json();

        
        const counts = {};
        posts.forEach(p => {
            counts[p.userId] = (counts[p.userId] || 0) + 1;
        });

        
        const result = users.map(u => ({
            name: u.name,
            count: counts[u.id] || 0
        })).filter(u => u.count > 0);

        
        result.sort((a, b) => b.count - a.count);

        
        console.log("Top 3 active users:");
        for (let i = 0; i < 3 && i < result.length; i++) {
            const u = result[i];
            console.log(`${i + 1}. ${u.name} - ${u.count} posts`);
        }

    } catch (error) {
        console.log("Something broke:", error.message);
    }
})();