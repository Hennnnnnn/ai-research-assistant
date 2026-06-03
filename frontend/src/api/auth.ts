import client from "./client";

export interface LoginRequest {
  email: string;
  password: string;
}

export async function login(
  data: LoginRequest
) {
  const response = await client.post(
    "/auth/login",
    data
  );

  return response.data;
}

export async function getCurrentUser() {
  const response = await client.get(
    "/users/me"
  );

  return response.data;
}