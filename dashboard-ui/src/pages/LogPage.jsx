import { useEffect, useState } from "react";
import { fetchLogs } from "../services/api";
import LogTable from "../components/LogTable";

export default function LogPage() {
  const [logs, setLogs] = useState([]);
  useEffect(() => {
    fetchLogs().then(data => setLogs(data));
  }, []);
  return (
    <div style={{ padding: "20px" }}>
      <h2>Logs</h2>
      <LogTable logs={logs} />
    </div>
  );
}
