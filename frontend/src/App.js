import { useState } from "react";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";

export default function App() {
  const [email, setEmail] = useState(null);

  return email ? (
    <Dashboard email={email} />
  ) : (
    <Login setEmail={setEmail} />
  );
}