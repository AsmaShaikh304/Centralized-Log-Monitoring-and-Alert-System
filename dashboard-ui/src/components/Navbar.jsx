export default function Navbar({ styleType = "default" }) {
  const styles = {
    default: { background: "#1e1e1e", color: "white" },
    material: { background: "#1976d2", color: "white" },
    tailwind: { background: "#f3f4f6", color: "black" },
    dark: { background: "#0f111a", color: "#39ff14" }
  };

  return (
    <div style={{ padding: "10px 20px", fontSize: "18px", ...styles[styleType] }}>
      CLMAS Dashboard
    </div>
  );
}
