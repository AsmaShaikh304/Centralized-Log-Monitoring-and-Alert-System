import { Link } from "react-router-dom";

export default function Sidebar({ styleType = "default" }) {
  const bgColors = {
    default: "#f5f5f5",
    material: "#eeeeee",
    tailwind: "#f9fafb",
    dark: "#11111f"
  };
  const textColors = {
    default: "black",
    material: "black",
    tailwind: "black",
    dark: "#39ff14"
  };

  return (
    <div style={{
      width: "200px",
      background: bgColors[styleType],
      color: textColors[styleType],
      height: "100vh",
      padding: "20px",
      borderRight: "1px solid #ccc"
    }}>
      <h3>Menu</h3>
      <ul style={{ listStyle: "none", padding: 0 }}>
        <li><Link to="/dashboard" style={{ color: textColors[styleType] }}>Dashboard</Link></li>
        <li><Link to="/logs" style={{ color: textColors[styleType] }}>Logs</Link></li>
        <li><Link to="/alerts" style={{ color: textColors[styleType] }}>Alerts</Link></li>
      </ul>
    </div>
  );
}
