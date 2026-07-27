export async function fetchEchoReferences() {
  try {
    const response = await fetch('/data/echo_references.json');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Failed to fetch echo references:", error);
    return null;
  }
}
