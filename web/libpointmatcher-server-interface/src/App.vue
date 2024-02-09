<template>
  <div>
    <SignIn @login-event="login_" :loginError="loginErrorMessage" />
  </div>
</template>

<script>
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
      loginErrorMessage: '',
    }
  },
  methods: {
    async register_(username, email, password) {
      await register(username, email, password);
    },
    async login_(email, password) {
      const response = await login(email, password);
    if (response.success) {
      this.loginErrorMessage = '';
      this.$router.push('/home');
    } else {
      this.loginErrorMessage = response.error;
    }
    },
    async logout_() {
      await logout();
    }
  }
};

</script>