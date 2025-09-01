import { useState } from "react";

function App() {
  const [level, setLevel] = useState("");
  const [time_in_sec, setTimeInSec] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  async function calculate() {
    try {
      const res = await fetch("http://127.0.0.1:5000/calculate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
          level: Number(level),
          time_in_sec: Number(time_in_sec)
        })
      });

      const data = await res.json();
      if (res.ok) {
        setResult(data.result);  // array
        setError("");
      } else {
        setError(data.error || "Backend error");
        setResult(null);
      }
  } catch (err) {
    setError("Error connecting to backend");
    setResult(null);
  }
}

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Calculator</h1>
      <label>
        Level: 
        <input
          type="number"
          value={level}
          onChange={(e) => setLevel(e.target.value)}
          placeholder="e.g. 1-12"
        />
      </label>

      <div>
        <label>
          Time (seconds):
          <input
            type="number"
            value={time_in_sec}
            onChange={(e) => setTimeInSec(e.target.value)}
            placeholder="Enter time in seconds"
          />
        </label>
      </div>

      <button onClick={calculate}>=</button>
      {error && <p>{error}</p>}

        {result && (
          <div>
            <h2>Results:</h2>
            <ul>
              {result.map(([name, info]) => (
                <li key={name}>
                  <strong>{name}</strong> - Activation Count: {info.activation_count}, Total Points: {info.point_total}
                </li>
              ))}
            </ul>
          </div>
        )}
    </div>
  );
}

export default App;