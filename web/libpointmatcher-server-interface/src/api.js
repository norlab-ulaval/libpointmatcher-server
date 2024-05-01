import Cookies from 'js-cookie'
import { useAuthStore } from '@/stores/authStore';
import router from './router'
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
  console.log("Token on login:", Cookies.get('token'));
  const formData = new FormData();
  formData.append("username", email);
  formData.append("password", password);
  
  try {
    const response = await fetch(`${endpoint}/login`, {
      method: "POST",
      body: formData,
    });

    const jsonResponse = await response.json();
    console.log("response")
    console.log(jsonResponse)

    if (!response.ok) {
      throw new Error(jsonResponse.detail || "Login failed");
    } 

    return { success: true, token: jsonResponse.access_token };
  } catch (error) {
    return { success: false, error: error.message };
  }
};

export const logout = async () => {
  const token = Cookies.get("token");
  
  try {
    const jsonResponse = await fetchWithAuth(`${endpoint}/logout`, {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${token}`,
      },
    });
    return { success: true };
  } catch (error) {
    return { success: false, error: "Network error or server is unreachable." };
  }
};

export const getLeaderboard = async (page, limit, type) => {

  try {
    const request = new Request(`${endpoint}/leaderboard?page=${page}&limit=${limit}&type=${type}`, {
      method: "GET",
    });

    const response = await fetch(request);
    const jsonResponse = await response.json();
    console.log("response")
    console.log(jsonResponse)

    if (!response.ok) {
      throw new Error(jsonResponse.detail || "Failed to fetch leaderboard.");
    }
    
    return { success: true, leaderboard: jsonResponse };
  } catch (error) {
    return { success: false, error: "Network error or server is unreachable." };
  }
};

export const getScoreTypes = async () => {
  
  try {
    const request = new Request(`${endpoint}/leaderboard/types`, {
      method: "GET",
    });

    const response = await fetch(request);
    const scoreTypes = await response.json();

    console.log(scoreTypes)
    if (!response.ok) {
      throw new Error(scoreTypes.detail || "Failed to fetch score types.");
    }
    
    return { success: true, types: scoreTypes };
  } catch (error) {
    return { success: false, error: "Network error or server is unreachable." };
  }
};


export const transferFile = async (configBase64, anonymousBool, filename) => {
  const token = Cookies.get("token");

  try {
    const jsonResponse = await fetchWithAuth(`${endpoint}/evaluation`, {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${token}`,
        "content-type": "application/json"
      },
      body: JSON.stringify({ config: configBase64, anonymous: anonymousBool, name: filename})
    });

    return { success: true };
  } catch (error) {
    return { success: false, error: "Network error or server is unreachable."};
  }
}

export const getRuns = async () => {
  const token = Cookies.get("token");

  try {
    const jsonResponse = await fetchWithAuth(`${endpoint}/run`, {
      method: "GET",
      headers: {
        "Authorization": `Bearer ${token}`,
      },
    });

    return { success: true, runs: jsonResponse };
  } catch (error) {
    return { success: false, error: "Network error or server is unreachable."};
  }
}

export const getFiles = async () => {
  try {
    const request = new Request(`${endpoint}/files`, {
      method: "GET",
      headers: {
        "content-type": "application/json"
      },
    });

    const response = await fetch(request);
    const jsonResponse = await response.json();

    if (!response.ok) {
      throw new Error(jsonResponse.detail || "Failed to get evaluations. Please try again.");
    }

    return { success: true, files: jsonResponse };
  } catch (error) {
    return { success: false, error: "Network error or server is unreachable."};
  }
}

async function fetchWithAuth(url, options) {
  const response = await fetch(url, options);
  const jsonResponse = await response.json();

  if (!response.ok) {
    if (response.status === 401) {
      console.log('401 interceptes')
      const store = useAuthStore();
      store.logout();
      router.push({ name: 'auth'});
    }
    console.log('test')
    throw new Error(jsonResponse.detail || jsonResponse.message || "An error occurred");
  }

  return jsonResponse;
}