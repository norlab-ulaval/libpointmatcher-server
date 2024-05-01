import { reactive } from 'vue';
import Cookies from 'js-cookie';

export const authStore = reactive({
    isLoggedIn: !!Cookies.get('token'),

    login(token) {
        Cookies.set('token', token, { expires: 1, secure: true });
        this.isLoggedIn = true;
    },

    logout() {
        Cookies.remove('token');
        this.isLoggedIn = false;
    },

    checkAuth() {
        this.isLoggedIn = !!Cookies.get('token');
    }
});