const express = require("express");
const path = require("path");
const bookings = require("./data/bookings.json");

const app = express();
const PORT = 3001;

// Serve static files from the public folder
app.use(express.static(path.join(__dirname, "public")));

// GET /data — returns the JSON bookings data
app.get("/data", (req, res) => {
  res.json(bookings);
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
