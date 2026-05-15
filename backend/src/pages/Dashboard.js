import { useEffect, useState } from "react";
import { getProfile, getBookings } from "../api";

export default function Dashboard({ email }) {
  const [profile, setProfile] = useState(null);
  const [bookings, setBookings] = useState([]);

  useEffect(() => {
    getProfile(email).then(res => setProfile(res.data));
    getBookings(email).then(res => setBookings(res.data.bookings));
  }, [email]);

  return (
    <div>
      <h1>Dashboard</h1>

      {profile && (
        <div>
          <p>{profile.firstName} {profile.lastName}</p>
          <p>{profile.email}</p>
        </div>
      )}

      <h2>Bookings</h2>
      {bookings.map((b, i) => (
        <div key={i}>
          {b.stock?.offer?.name} - {b.dateUsed}
        </div>
      ))}
    </div>
  );
}