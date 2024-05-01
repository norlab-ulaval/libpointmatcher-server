import Vue from 'vue';
import Vuex from 'vuex';
import Cookies from 'js-cookie';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isLoggedIn: false
  },
  mutations: {
    setLoggedIn(state, isLoggedIn) {
      state.isLoggedIn = isLoggedIn;
    }
  },
  actions: {
    checkLogin({ commit }) {
      const token = Cookies.get('token');
      commit('setLoggedIn', validateToken(token));
    },
    login({ commit }, token) {
      Cookies.set('token', token, { expires: 1, secure: true });
      commit('setLoggedIn', true);
    },
    logout({ commit }) {
      Cookies.remove('token');
      commit('setLoggedIn', false);
    }
  },
  getters: {
    isLoggedIn: state => state.isLoggedIn
  }
});

function validateToken(token) {
    if (!token) {
        return false;
    }

    const tokenPayload = parseJwt(token);
    if (tokenPayload && tokenPayload.exp * 1000 > Date.now()) {
        return true;
    }
    return false;
}

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