import {
    useState,
} from "react";

import {
    Navigate,
    useNavigate,
} from "react-router-dom";

import {
    useAuth,
} from "../hooks/useAuth";

export default function Login() {
    const navigate =
        useNavigate();

    const {
        loginUser,
        isAuthenticated,
        loading,
    } = useAuth();

    const [email, setEmail] =
        useState("");

    const [password, setPassword] =
        useState("");

    const [error, setError] = useState("")
    const [submitting, setSubmitting] = useState(false);

    async function handleSubmit(
        e: React.FormEvent
    ) {
        e.preventDefault();
        setSubmitting(true)
        try {
            await loginUser(
                email,
                password
            );

            navigate("/");
        } catch {
            setError("Invalid email or password")
        } finally {
            setSubmitting(false)
        }

    }

    if (loading) {
        return <div>Loading...</div>;
    }

    if (isAuthenticated) {
        return <Navigate to="/" replace />;
    }

    return (
        <form
            onSubmit={
                handleSubmit
            }
        >
            <input
                value={email}
                onChange={(e) =>
                    setEmail(
                        e.target.value
                    )
                }
            />

            <input
                type="password"
                value={password}
                onChange={(e) =>
                    setPassword(
                        e.target.value
                    )
                }
            />

            <button disabled={submitting}>
                {submitting ? "Logging in..." : "Login"}
            </button>
            {error && <p>{error}</p>}
        </form>
    );
}