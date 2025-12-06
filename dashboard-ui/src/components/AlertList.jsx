export default function AlertList({ alerts }) {
  return (
    <ul>
      {alerts.map((alert, i) => (
        <li key={i}>
          <strong>{alert.ruleName}</strong> - {alert.message}
        </li>
      ))}
    </ul>
  );
}
