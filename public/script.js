const categoryEmoji = (category) => {
  const map = {
    "Musique": "🎵",
    "Exposition": "🖼",
    "Livre": "📚",
    "Cinéma": "🎬",
    "Atelier": "🎨",
    "Spectacle": "🎭",
    "Jeu": "🎮",
  };
  return map[category] || "🎟";
};

const fetchBookings = async () => {
  const btn = document.getElementById("fetch-btn");
  const result = document.getElementById("result");

  btn.disabled = true;
  btn.textContent = "Chargement...";
  result.style.display = "none";
  result.innerHTML = "";

  try {
    const response = await fetch("/data");
    const bookings = await response.json();

    result.style.display = "flex";

    bookings.forEach((booking) => {
      const tagClass = booking.status === "Utilisé" ? "tag-used" : "tag-reserved";

      const item = document.createElement("div");
      item.className = "booking-item";
      item.innerHTML = `
        <div class="booking-emoji">${categoryEmoji(booking.category)}</div>
        <div class="booking-info">
          <div class="booking-title">${booking.title}</div>
          <div class="booking-meta">${booking.location} · ${booking.date}</div>
        </div>
        <span class="tag ${tagClass}">${booking.status}</span>
        <div class="booking-price">${booking.price.toFixed(2)} €</div>
      `;
      result.appendChild(item);
    });

    btn.textContent = "Actualiser";
  } catch (error) {
    result.style.display = "flex";
    result.innerHTML = `<p style="color:#f87171">Erreur lors du chargement des données.</p>`;
    btn.textContent = "Réessayer";
  } finally {
    btn.disabled = false;
  }
};

document.getElementById("fetch-btn").addEventListener("click", fetchBookings);
