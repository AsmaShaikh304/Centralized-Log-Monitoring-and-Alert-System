export default function LogTable({ logs }) {
  return (
    <table style={{ width: "100%", borderCollapse: "collapse" }}>
      <thead>
        <tr style={{ background: "#ddd" }}>
          <th>Timestamp</th>
          <th>Level</th>
          <th>Message</th>
          <th>Source</th>
        </tr>
      </thead>
      <tbody>
        {logs.map((log, i) => (
          <tr key={i} style={{ borderBottom: "1px solid #ccc" }}>
            <td>{log.timestamp}</td>
            <td>{log.level}</td>
            <td>{log.message}</td>
            <td>{log.source}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
