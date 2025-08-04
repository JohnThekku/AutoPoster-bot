document.getElementById("trigger").addEventListener("click", () => {
    fetch("http://127.0.0.1:5000/rewrite", {
      method: "POST"
    })
    .then(res => res.text())
    .then(data => {
      document.getElementById("status").textContent = data;
    })
    .catch(err => {
      document.getElementById("status").textContent = "Server not running";
    });
  });
  