import { defineStore } from 'pinia';
import Cookies from 'js-cookie';

function parseJwt(token) {
    try {
        const base64Url = token.split('.')[1];
        const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
        const jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
            return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
        }).join(''));


        return JSON.parse(jsonPayload);
    } catch (e) {
        return null;
    }
  }
  
export const useAuthStore = defineStore('auth', {
    state: () => ({
      isLoggedIn: false
    }),
    getters: {
      isAuthenticated: (state) => state.isLoggedIn
    },
    actions: {
      login(token) {
        Cookies.set('token', token, { expires: 1, secure: true });
        this.isLoggedIn = true;
      },
      logout() {
        Cookies.remove('token');
        this.isLoggedIn = false;
      },
      checkAuth() {
        const token = Cookies.get('token');
        this.isLoggedIn = this.validateToken(token);
      },
      validateToken(token) {
        if (!token) {
            return false;
        }
    
        const tokenPayload = parseJwt(token);
        if (tokenPayload && tokenPayload.exp * 1000 > Date.now()) {
            return true;
        }
        return false;
      },
      
    },
    
  });