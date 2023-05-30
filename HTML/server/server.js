const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const fs = require("fs");

const app = express();
app.use(bodyParser.json());
app.use(cors());

let data = require("./data.json");

app.get("/data.json", (req, res) => {
  res.json(data);
});

app.post("/booking", (req, res) => {
  try {
    // Get existing booking data, and push new booking to list. 
    let existingBookings = JSON.parse(fs.readFileSync("./data.json", "utf8"));
    const newBooking = req.body;
    existingBookings.bookings.push(newBooking);
    fs.writeFileSync("./data.json", JSON.stringify(existingBookings));
    res.json(existingBookings);

  } catch (err) {
    console.error("Error reading or writing data:", err);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

app.listen(5000, () => {
  console.log("Server is running on port 5000");
});
