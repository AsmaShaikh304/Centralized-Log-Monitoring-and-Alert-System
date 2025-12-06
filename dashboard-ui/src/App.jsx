import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Sidebar from "./components/Sidebar";
import Dashboard from "./pages/Dashboard";
import LogPage from "./pages/LogPage";
import AlertPage from "./pages/AlertPage";

export default function App() {
  // You can change styleType to "material", "tailwind", or "dark"
  const styleType = "default";

  return (
    <BrowserRouter>
      <Navbar styleType={styleType} />
      <div style={{ display: "flex" }}>
        <Sidebar styleType={styleType} />
        <div style={{ flex: 1 }}>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/logs" element={<LogPage />} />
            <Route path="/alerts" element={<AlertPage />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
}
