import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

import { getResearchDetail } from "../api/research";

import type { Research } from "../types/research";
import { deleteResearch } from "../api/research";

import { useNavigate } from "react-router-dom";

export default function ResearchDetail() {
    const { id } = useParams();
    const navigate = useNavigate();

    const [research, setResearch] = useState<Research | null>(null);

    const [loading, setLoading] = useState(true);

    const [error, setError] = useState("");

    async function handleDelete() {
        if (!window.confirm(
            "Delete this research?"
        )) {
            return;
        }

        await deleteResearch(research!.id);

        navigate("/")
    }

    async function loadResearch() {
        try {
            setLoading(true);

            const data = await getResearchDetail(Number(id));

            setResearch(data);
        } catch (err) {
            setError("Failed to load research");

            console.error(err);
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        if (id) {
            loadResearch();
        }
    }, [id]);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>{error}</div>;
    }

    if (!research) {
        return <div>Research not found</div>;
    }

    return (
        <div>
            <button
                onClick={handleDelete}
            >
                Delete Research
            </button>
            
            <h1>{research.topic}</h1>

            <p>
                <strong>Created At:</strong>{" "}
                {new Date(research.created_at).toLocaleString()}
            </p>

            <hr />

            <h2>Summary</h2>

            <p>{research.summary}</p>
        </div>
    );
}
