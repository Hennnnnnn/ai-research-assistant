import { useEffect, useState } from "react";

import { createResearch, getResearchList } from "../api/research";

import { useAuth } from "../hooks/useAuth";
import type { ResearchListItem } from "../types/research";
import { Link } from "react-router-dom";

export default function Dashboard() {
  const { user, logout } = useAuth();

  const [topic, setTopic] = useState("");
  const [page, setPage] = useState(1);

  const [total, setTotal] = useState(0);

  const pageSize = 10;
  const [researches, setResearches] = useState<ResearchListItem[]>([]);
  const [search, setSearch] = useState("");
  const [debouncedSearch, setDebouncedSearch] = useState("");

  useEffect(() => {
    const timer =
      setTimeout(() => {
        setDebouncedSearch(
          search
        );
      }, 500);

    return () => {
      clearTimeout(timer);
    };
  }, [search]);

  async function loadResearches() {
    const data = await getResearchList(
      debouncedSearch,
      page,
      pageSize
    );

    setResearches(data.items);
    setTotal(data.total);
  }

  async function handleGenerate() {
    if (!topic.trim()) {
      return;
    }

    await createResearch({
      topic,
    });

    setTopic("");

    setPage(1);
  }

  useEffect(() => {
    const interval =
      setInterval(() => {
        void loadResearches();
      }, 5000);

    return () =>
      clearInterval(interval);
  }, []);

  useEffect(() => {
    void loadResearches();
  }, [page, debouncedSearch]);

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

      <input
        value={search}
        onChange={(e) => {
          setSearch(e.target.value)
          setPage(1)
        }}
        placeholder="Search research..."
      />

      <ul>
        {researches.map((research) => (
          <li key={research.id}>
            <Link
              to={`/research/${research.id}`}
            >
              {research.topic}
            </Link>

            {" "}

            {research.status === "completed" && (
              <span>🟢 Completed</span>
            )}

            {research.status === "processing" && (
              <span>🟡 Processing</span>
            )}

            {research.status === "failed" && (
              <span>🔴 Failed</span>
            )}
          </li>
        ))}
      </ul>
      <div>
        <button
          disabled={page === 1}
          onClick={() =>
            setPage(
              page - 1
            )
          }
        >
          Previous
        </button>

        <span>
          Page {page}
        </span>

        <button
          disabled={
            page * pageSize >=
            total
          }
          onClick={() =>
            setPage(
              page + 1
            )
          }
        >
          Next
        </button>
      </div>
    </div>
  );
}
