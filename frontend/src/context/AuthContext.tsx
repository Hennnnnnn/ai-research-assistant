import {
  useEffect,
  useState,
} from "react";
import type { ReactNode } from "react";

import { login, getCurrentUser } from "../api/auth";

import {
  saveToken,
  removeToken,
  getToken,
} from "../utils/token";
import { AuthContext } from "./auth-context";
import type { User } from "../types/user";

interface Props {
  children: ReactNode;
}

export function AuthProvider({
  children,
}: Props) {
  const [user, setUser] =
    useState<User | null>(null);

  const [loading, setLoading] =
    useState(() => !!getToken());

  async function loginUser(
    email: string,
    password: string
  ) {
    const response = await login({
      email,
      password,
    });

    saveToken(response.access_token);

    const currentUser =
      await getCurrentUser();

    setUser(currentUser);
  }

  function logout() {
    removeToken();
    setUser(null);
  }

  useEffect(() => {
    const token = getToken();

    if (!token) {
      return;
    }

    let active = true;

    getCurrentUser()
      .then((currentUser) => {
        if (active) {
          setUser(currentUser);
        }
      })
      .catch(() => {
        if (active) {
          removeToken();
          setUser(null);
        }
      })
      .finally(() => {
        if (active) {
          setLoading(false);
        }
      });

    return () => {
      active = false;
    };
  }, []);

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        isAuthenticated: !!user,
        loginUser,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}