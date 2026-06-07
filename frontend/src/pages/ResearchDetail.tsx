import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'

import { exportResearchPDF, getResearchDetail } from '../api/research'

import type { Research } from '../types/research'
import { deleteResearch } from '../api/research'

import { useNavigate } from 'react-router-dom'

export default function ResearchDetail() {
    const { id } = useParams()
    const navigate = useNavigate()

    const [research, setResearch] = useState<Research | null>(null)

    const [loading, setLoading] = useState(true)

    const [error, setError] = useState('')

    async function handleDelete() {
        if (!window.confirm('Delete this research?')) {
            return
        }

        await deleteResearch(research!.id)

        navigate('/')
    }

    useEffect(() => {
        if (!id) {
            return
        }

        async function fetchResearch() {
            try {
                setLoading(true)

                const data = await getResearchDetail(Number(id))

                setResearch(data)
            } catch (err) {
                setError('Failed to load research')

                console.error(err)
            } finally {
                setLoading(false)
            }
        }

        fetchResearch()
    }, [id])

    async function handleExport() {
        if (!research) {
            return;
        }

        try {
            const response =
                await exportResearchPDF(
                    research.id
                );

            const url =
                window.URL.createObjectURL(
                    response.data
                );

            const link =
                document.createElement(
                    "a"
                );

            link.href = url;

            link.download =
                `${research.topic}.pdf`;

            document.body.appendChild(
                link
            );

            link.click();

            link.remove();

            window.URL.revokeObjectURL(
                url
            );
        } catch (err) {
            console.error(err);

            alert(
                "Failed to export PDF"
            );
        }
    }

    if (loading) {
        return <div>Loading...</div>
    }

    if (error) {
        return <div>{error}</div>
    }

    if (!research) {
        return <div>Research not found</div>
    }

    return (
        <div>
            <div>
                <button
                    onClick={
                        handleExport
                    }
                >
                    Export PDF
                </button>

                <button
                    onClick={
                        handleDelete
                    }
                >
                    Delete Research
                </button>
            </div>
            <h1>{research.topic}</h1>

            <p>
                <strong>Created At:</strong>{' '}
                {new Date(research.created_at).toLocaleString()}
            </p>

            <hr />

            <h2>Overview</h2>

            <p>{research.research_data.overview}</p>

            <hr />

            <h2>Key Findings</h2>

            <ul>
                {research.research_data.key_findings.map((finding, index) => (
                    <li key={index}>{finding}</li>
                ))}
            </ul>

            <hr />

            <h2>Risks</h2>

            <ul>
                {research.research_data.risks.map((risk, index) => (
                    <li key={index}>{risk}</li>
                ))}
            </ul>

            <hr />

            <h2>Future Trends</h2>

            <ul>
                {research.research_data.future_trends.map((trend, index) => (
                    <li key={index}>{trend}</li>
                ))}
            </ul>

            <h2>Sources</h2>

            <ul>
                {(research.research_data.sources ?? []).map(
                    (source, index) => (
                        <li key={index}>
                            <a
                                href={source.url}
                                target="_blank"
                                rel="noreferrer"
                            >
                                {source.title}
                            </a>
                        </li>
                    )
                )}
            </ul>
        </div>
    )
}
