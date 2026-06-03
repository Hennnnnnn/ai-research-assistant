import {
  Navigate,
} from "react-router-dom";

import { useAuth } from "../hooks/useAuth";
import type { JSX } from "react/jsx-runtime";

interface Props {
  children: JSX.Element;
}

export default function ProtectedRoute({
  children,
}: Props) {
  const {
    isAuthenticated,
    loading,
  } = useAuth();

  if (loading) {
    return <div>Loading...</div>;
  }

  if (!isAuthenticated) {
    return (
      <Navigate
        to="/login"
      />
    );
  }

  return children;
}