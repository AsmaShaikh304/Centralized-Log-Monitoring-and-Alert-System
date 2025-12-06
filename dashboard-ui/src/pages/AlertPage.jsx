import { useEffect, useState } from "react";
import { fetchAlerts } from "../services/api";

export default function AlertPage() {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    fetchAlerts().then(data => setAlerts(data));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Alerts</h2>
      <ul>
        {alerts.map((alert, index) => (
          <li key={index}>
            <strong>{alert.ruleName}</strong> - {alert.message}
          </li>
        ))}
      </ul>
    </div>
  );
}
