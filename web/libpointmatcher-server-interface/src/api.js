import Cookies from 'js-cookie'

const endpoint = 'http://localhost:8000';

export const register = async (name, email, password) => {
  try {
    const request = new Request(`${endpoint}/register`, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ username: name, email, email, password: password }),
    });
    const response = await fetch(request);
    if (!response.ok) {
      throw new Error("Failed to register. Please try again.");
    }
    const jsonResponse = await response.json();
    return { success: true };
  } catch (error) {
    console.error(error);
    return { success: false, error: error.message || "An error occurred during registration." };
  }
};

export const login = async (email, password) => {
  try {
    const request = new Request(`${endpoint}/login`, {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    });

    const response = await fetch(request);
    const jsonResponse = await response.json();

    if (response.ok) {
      Cookies.set("token", jsonResponse.token, { expires: 1 });
      return { success: true };
    } else {
      return { success: false, error: jsonResponse.message || "Login failed"};
    }
  } catch (error) {
    return { success: false, error: "Network error or server is unreachable." };
  }
};

export const logout = async () => {
    // À modifier
    Cookies.remove("token");
  };