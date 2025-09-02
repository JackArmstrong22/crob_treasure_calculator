import { useState } from "react";
import "./App.css";

function App() {
  const [level, setLevel] = useState("");
  const [time_in_sec, setTimeInSec] = useState("");
  const [is_bonus_time, setBonusTime] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");

  async function calculate() {
    try {
      const res = await fetch("http://127.0.0.1:5000/calculate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          level: Number(level),
          time_in_sec: Number(time_in_sec),
          is_bonus_time: is_bonus_time
        })
      });

      const data = await res.json();
      if (res.ok) {
        setResult(data.result); // list of [name, info] pairs
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
    <div className="app-container">
      <h1>Calculator</h1>

      <div className="input-group">
        <label>
          Treasure Level:
          <input
            type="number"
            value={level}
            onChange={(e) => setLevel(e.target.value)}
            placeholder="e.g. 1-12"
          />
        </label>
      </div>

      <div className="input-group">
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

      <div className="input-group">
        <label>
          Is There a Bonus Time?
          <input
            type="checkbox"
            value={is_bonus_time}
            onChange={(e) => setBonusTime(e.target.checked)}
          />
        </label>
      </div>

      <button className="calculate-button" onClick={calculate}>Calculate!</button>

      {error && <p className="error">{error}</p>}

      {Array.isArray(result) && result.length > 0 && (
        <div className="results-container">
          <h2>Results:</h2>
          <ol type="1" className="results-list">
            {result.map(([, info], index) => {
              const imageName = info.treasure.toLowerCase().replace(/ /g, "_");
              const imageUrl = `/images/${imageName}.png`;

              return (
                <li key={info.treasure} className="result-item">
                  {/* Numbered list */}
                  <span className="result-number">{index + 1}.</span>
                  <img
                    src={imageUrl}
                    alt={info.treasure}
                    width={50}
                    height={50}
                    onError={(e) => { e.target.onerror = null; e.target.src = "/images/default.png"; }}
                  />
                  <div className="result-text">
                    <strong>{info.treasure}</strong> - Activation Count: {info.activation_count}, Total Points: {info.point_total.toLocaleString()}
                  </div>
                </li>
              );
            })}
          </ol>
        </div>
      )}
    </div>
  );
}

export default App;