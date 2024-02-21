import Cookies from 'js-cookie'

const endpoint = import.meta.env.VITE_API_URI;

export const register = async (name, email, password) => {
  try {
    const request = new Request(`${endpoint}/register`, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify({ username: name, email: email, password: password }),
    });
    const response = await fetch(request);
    
    const jsonResponse = await response.json();

    if (!response.ok) {
      throw new Error(jsonResponse.detail || "Failed to register. Please try again.");
    }

    return { success: true };
  } catch (error) {
    console.error(error);
    return { success: false, error: error.message };
  }
};


export const login = async (email, password) => {
  const formData = new FormData();
  formData.append("username", email);
  formData.append("password", password);
  
  try {
    const response = await fetch(`${endpoint}/login`, {
      method: "POST",
      body: formData,
    });

    const jsonResponse = await response.json();

    if (response.ok) {
      Cookies.set("token", jsonResponse.token, { expires: 1 }, { secure: true });
      return { success: true };
    } else {
      return { success: false, error: jsonResponse.detail || "Login failed"};
    }
  } catch (error) {
    return { success: false, error: "Network error or server is unreachable." };
  }
};

export const logout = async () => {
    // À modifier
    Cookies.remove("token");
};

export const getLeaderboard = async (page, limit, type) => {
  const token = Cookies.get("token");
  
  try {
    const request = new Request(`${endpoint}/leaderboard`, {
      method: "GET",
      headers: {
        "content-type": "application/json",
        "Authorization": `Bearer ${token}`,
      },
      body: JSON.stringify({ page: page, limit: limit, type: type }),
    });

    const response = await fetch(request);
    const jsonResponse = await response.json();

    if (response.ok) {
      return { success: true, leaderboard: jsonResponse };
    }
    else {
      return { success: false, error: jsonResponse.detail || "Failed to fetch leaderboard." };
    }
  } catch (error) {
    return { success: false, error: "Network error or server is unreachable." };
  }
}