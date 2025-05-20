// index.js

import { useEffect, useState } from 'react';

export default function Home() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/hello`)
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch(() => setMessage("Error fetching data"));
  }, []);

  return (
    <div>
      <h1>Physics Formula Viewer</h1>
      <p>Backend says: {message}</p>
    </div>
  );
}
