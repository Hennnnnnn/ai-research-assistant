import { createContext } from "react";
import type { User } from "../types/user";

export interface AuthContextType {
  user: User | null;
  loading: boolean;
  isAuthenticated: boolean;
  loginUser: (
    email: string,
    password: string
  ) => Promise<void>;
  logout: () => void;
}

const defaultAuthContext: AuthContextType = {
  user: null,
  loading: true,
  isAuthenticated: false,
  loginUser: async () => {},
  logout: () => {},
};

export const AuthContext =
  createContext<AuthContextType>(
    defaultAuthContext
  );
