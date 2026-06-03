import { useEffect, useState } from "react";

import { createResearch, getResearchList } from "../api/research";

import { useAuth } from "../hooks/useAuth";
import type { ResearchListItem } from "../types/research";
import { Link } from "react-router-dom";

export default function Dashboard() {
  const { user, logout } = useAuth();

  const [topic, setTopic] = useState("");

  const [researches, setResearches] = useState<ResearchListItem[]>([]);

  async function loadResearches() {
    const data = await getResearchList();

    setResearches(data);
  }

  async function handleGenerate() {
    if (!topic.trim()) return;

    await createResearch({
      topic,
    });

    setTopic("");

    await loadResearches();
  }

  useEffect(() => {
    loadResearches();
  }, []);

  return (
    <div>
      <h1>Welcome {user?.username}</h1>

      <p>{user?.email}</p>

      <button onClick={logout}>Logout</button>

      <hr />

      <h2>Create Research</h2>

      <input
        value={topic}
        onChange={(e) => setTopic(e.target.value)}
        placeholder="Enter research topic"
      />

      <button onClick={handleGenerate}>Generate Research</button>

      <hr />

      <h2>Research History</h2>

      <ul>
        {researches.map((research) => (
          <li key={research.id}>
            <Link
              to={`/research/${research.id}`}
            >
              {research.topic}
            </Link>
          </li>))}
      </ul>
    </div>
  );
}
