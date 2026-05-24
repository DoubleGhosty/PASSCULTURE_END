import { useState } from "react";
import { login } from "../api";
import "./Login.css";

export default function Login({ setEmail }) {
  const [email, setE] = useState("");
  const [password, setP] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handle = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    try {
      await login(email, password);
      setEmail(email);
    } catch (err) {
      setError("Email ou mot de passe incorrect.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="login-root">
      <div className="login-card">
        <div className="login-logo">
          <span className="login-logo-text">PASS</span>
        </div>

        <h1 className="login-title">Connexion</h1>
        <p className="login-subtitle">Accédez à votre espace personnel</p>

        <form className="login-form" onSubmit={handle}>
          <div className="login-field">
            <label htmlFor="email">Adresse email</label>
            <input
              id="email"
              type="email"
              placeholder="vous@exemple.com"
              value={email}
              onChange={(e) => setE(e.target.value)}
              required
            />
          </div>

          <div className="login-field">
            <label htmlFor="password">Mot de passe</label>
            <input
              id="password"
              type="password"
              placeholder="••••••••"
              value={password}
              onChange={(e) => setP(e.target.value)}
              required
            />
          </div>

          {error && <p className="login-error">{error}</p>}

          <button className="login-btn" type="submit" disabled={loading}>
            {loading ? <span className="login-spinner" /> : "Se connecter"}
          </button>
        </form>
      </div>
    </div>
  );
}
