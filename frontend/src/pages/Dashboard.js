import { useEffect, useState } from "react";
import { getProfile, getBookings } from "../api";
import "./Dashboard.css";

export default function Dashboard({ email }) {
  const [profile, setProfile] = useState(null);
  const [bookings, setBookings] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([
      getProfile(email),
      getBookings(email)
    ]).then(([profileRes, bookingsRes]) => {
      setProfile(profileRes.data);
      setBookings(bookingsRes.data.bookings || []);
    }).finally(() => setLoading(false));
  }, [email]);

  if (loading) {
    return (
      <div className="dash-root">
        <div className="dash-loading">
          <span className="dash-spinner" />
          <p>Chargement...</p>
        </div>
      </div>
    );
  }

  const credit = profile?.domainsCredit?.all?.remaining;

  return (
    <div className="dash-root">
      <div className="dash-container">

        {/* HEADER */}
        <header className="dash-header">
          <span className="dash-logo">PASS</span>
          <div className="dash-avatar">
            {profile?.firstName?.[0]}{profile?.lastName?.[0]}
          </div>
        </header>

        {/* PROFILE CARD */}
        {profile && (
          <div className="dash-profile-card">
            <div className="dash-profile-info">
              <h2 className="dash-profile-name">
                {profile.firstName} {profile.lastName}
              </h2>
              <p className="dash-profile-email">{profile.email}</p>
            </div>
            {credit != null && (
              <div className="dash-credit">
                <span className="dash-credit-amount">{(credit / 100).toFixed(2)} €</span>
                <span className="dash-credit-label">crédit restant</span>
              </div>
            )}
          </div>
        )}

        {/* BOOKINGS */}
        <section className="dash-section">
          <h3 className="dash-section-title">
            Mes réservations
            <span className="dash-badge">{bookings.length}</span>
          </h3>

          {bookings.length === 0 ? (
            <div className="dash-empty">Aucune réservation trouvée.</div>
          ) : (
            <div className="dash-bookings">
              {bookings.map((b, i) => (
                <div key={i} className="dash-booking-card">
                  <div className="dash-booking-icon">
                    {categoryIcon(b.stock?.offer?.subcategoryId)}
                  </div>
                  <div className="dash-booking-info">
                    <p className="dash-booking-name">
                      {b.stock?.offer?.name || "Offre inconnue"}
                    </p>
                    <p className="dash-booking-date">
                      {b.dateUsed ? formatDate(b.dateUsed) : "Date non renseignée"}
                    </p>
                  </div>
                  <div className={`dash-booking-status ${b.isUsed ? "used" : "pending"}`}>
                    {b.isUsed ? "Utilisé" : "Réservé"}
                  </div>
                </div>
              ))}
            </div>
          )}
        </section>

      </div>
    </div>
  );
}

function formatDate(iso) {
  return new Date(iso).toLocaleDateString("fr-FR", {
    day: "numeric", month: "long", year: "numeric"
  });
}

function categoryIcon(subcategoryId) {
  if (!subcategoryId) return "🎟";
  const id = subcategoryId.toLowerCase();
  if (id.includes("cinema")) return "🎬";
  if (id.includes("concert") || id.includes("musique")) return "🎵";
  if (id.includes("livre") || id.includes("book")) return "📚";
  if (id.includes("jeu") || id.includes("game")) return "🎮";
  if (id.includes("spectacle") || id.includes("theatre")) return "🎭";
  if (id.includes("expo") || id.includes("musee")) return "🖼";
  return "🎟";
}
