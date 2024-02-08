import Cookies from 'js-cookie'

const endpoint = 'http://localhost:8000';

export const register = async (name, email, password) => {
    const request = new Request(`${endpoint}/register`, {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify({
        username: name,
        email: email,
        password: password,
      }),
    });
    const response = await fetch(request);
    const jsonResponse = await response.json();
    console.log(jsonResponse);
    return jsonResponse;
};

  export const login = async (email, password) => {
    const request = new Request(`${endpoint}/login`, {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify({
        email: email,
        password: password,
      }),
    });
    const response = await fetch(request);
    console.log(response);
    let jsonResponse = 401;
    if (response.status == 200) {
      jsonResponse = await response.json();
      Cookies.set("token", jsonResponse.token, {expires: 1});
    }
    return jsonResponse;
};

export const logout = async () => {
    // À modifier
    Cookies.remove("token");
  };