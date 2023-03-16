function updateTime() {
    fetch("https://10.0.0.151/push", {
        method: "POST",
        body: JSON.stringify({
            userId: 1,
            title: "Fix my bugs",
            completed: false
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
        })
        .then((response) => response.json())
        .then((json) => console.log(json));
}

updateTime();
setInterval(updateTime, 1000);