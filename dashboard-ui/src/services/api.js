const BASE_URL = "http://localhost:8080/api";

export async function fetchLogs() {
  const response = await fetch(`${BASE_URL}/logs`);
  return response.json();
}

export async function fetchAlerts() {
  const response = await fetch(`${BASE_URL}/alerts`);
  return response.json();
}
