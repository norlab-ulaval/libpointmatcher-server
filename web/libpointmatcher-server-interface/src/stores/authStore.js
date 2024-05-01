import { reactive } from 'vue';
import Cookies from 'js-cookie';
import { jwtDecode } from "jwt-decode";

export const authStore = reactive({
    isLoggedIn: checkInitialToken(),

    login(token) {
        console.log("Token before setting:", Cookies.get('token'));
        console.log(isLoggedIn)
        console.log(token.expires)
        Cookies.set('token', token, { expires: 1, secure: true });
        console.log("Token after setting:", Cookies.get('token'));
        console.log(isLoggedIn)
        this.isLoggedIn = true;
    },

    logout() {
        Cookies.remove('token');
        this.isLoggedIn = false;
    },

    checkAuth() {
        const token = Cookies.get('token');
        this.isLoggedIn = validateToken(token);
    }
});

function checkInitialToken() {
    const token = Cookies.get('token');
    return validateToken(token);
}

function validateToken(token) {
    if (token) {
        try {
            const decoded = jwtDecode(token);
            const currentTime = Date.now() / 1000;
            if (decoded.exp > currentTime) {
                return true;
            }
        } catch (error) {
            console.error("Token decoding failed:", error);
        }
    }
    return false;
}