<template>
  <div>
    <SignIn/>
  </div>
</template>

<script>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import SignIn from './components/SignIn.vue';
import { register, login, logout } from './api';

export default {
  name: "app",
  components: {
    SignIn
  },
  data() {
    return {
      username: '',
      email: '',
      password: '',
    }
  },
  methods: {
    async register_(username, email, password) {
      await register(username, email, password);
    },
    async login_(username, password) {
      await login(username, password);
    },
    async logout_() {
      await logout();
    }
  }
};

</script>