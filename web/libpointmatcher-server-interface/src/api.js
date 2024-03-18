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

    if (!response.ok) {
      throw new Error(jsonResponse.detail || "Login failed");
    } 

    Cookies.set("token", jsonResponse.access_token, { expires: 1 }, { secure: true });
    return { success: true };
  } catch (error) {
    return { success: false, error: error.message };
  }
};

export const logout = async () => {
  const token = Cookies.get("token");
  
  try {
    const request = new Request(`${endpoint}/logout`, {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${token}`,
      },
    });

    const response = await fetch(request);
    const jsonResponse = await response.json();

    if (!response.ok) {
      throw new Error(jsonResponse.detail || "Failed to logout.");
    }

    Cookies.remove("token");
    return { success: true };
  } catch (error) {
    return { success: false, error: "Network error or server is unreachable." };
  }
};

export const getLeaderboard = async (page, limit, type) => {
  const token = Cookies.get("token");
  
  try {
    const request = new Request(`${endpoint}/leaderboard?page=${page}&limit=${limit}&type=${type}`, {
      method: "GET",
      headers: {
        "content-type": "application/json",
        "Authorization": `Bearer ${token}`,
      }
    });

    const response = await fetch(request);
    const jsonResponse = await response.json();

    if (!response.ok) {
      throw new Error(jsonResponse.detail || "Failed to fetch leaderboard.");
    }
    
    return { success: true, leaderboard: jsonResponse };
  } catch (error) {
    return { success: false, error: "Network error or server is unreachable." };
  }
};

export const transferFile = async (configString, anonymousBool) => {
  const token = Cookies.get("token");

  try {
    const request = new Request(`${endpoint}/evaluation`, {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${token}`,
      },
      body: JSON.stringify({evaluation:{config: configString, anonymous: anonymousBool}})
    });

    const response = await fetch(request);
    const jsonResponse = await response.json();

    if (!response.ok) {
      throw new Error(jsonResponse.detail || "Failed to evaluate. Please try again.");
    }

    return { success: true };
  } catch (error) {
    return { success: false, error: "Network error or server is unreachable."};
  }
}
