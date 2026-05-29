import axios from "axios";

const API = "https://passculture-end.onrender.com";

export const login = (email, password) =>
  axios.post(`${API}/login`, { email, password });

export const getProfile = (email) =>
  axios.get(`${API}/profile/${email}`);

export const getBookings = (email) =>
  axios.get(`${API}/bookings/${email}`);