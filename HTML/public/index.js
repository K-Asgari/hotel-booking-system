const form = document.getElementById("booking-info");

form.addEventListener("submit", (e) => {
  e.preventDefault(); // Debugging -> Disables page redirect/refresh on submit

  const formData = new FormData(form);

  const name = formData.get("name");
  const phone = formData.get("phone");
  const checkIn = formData.get("check-in");
  const checkOut = formData.get("check-out");
  // Date format: YYYY-MM-DD

  const bookingInfoJSON = {
    "name": name,
    "phone": phone,
    "checkIn": checkIn,
    "checkOut": checkOut,
  };

  fetch("http://127.0.0.1:5000/booking", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(bookingInfoJSON),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Form data submitted:", data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});




