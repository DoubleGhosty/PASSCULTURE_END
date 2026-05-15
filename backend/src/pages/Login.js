import { useState } from "react";
import { login } from "../api";

export default function Login({ setEmail }) {
  const [email, setE] = useState("");
  const [password, setP] = useState("");

  const handle = async () => {
    await login(email, password);
    setEmail(email);
  };

  return (
    <div>
      <h1>Login</h1>
      <input placeholder="email" onChange={(e) => setE(e.target.value)} />
      <input placeholder="password" type="password" onChange={(e) => setP(e.target.value)} />
      <button onClick={handle}>Login</button>
    </div>
  );
}