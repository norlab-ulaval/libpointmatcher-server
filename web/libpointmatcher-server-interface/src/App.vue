<template>
  <div>
    <SignIn @login-event="login_" :loginError="loginErrorMessage" v-if="!showSignUp" @toggle-signup="toggleSignUp" />
    <SignUp @signup-event="register_" :signUpError="signUpErrorMessage" v-else @back-to-signin="toggleSignUp" />
  </div>
</template>

<script>
import SignIn from './components/SignIn.vue';
import SignUp from './components/SignUp.vue';
import { register, login, logout } from './api';

export default {
  name: "app",
  components: {
    SignIn,
    SignUp
  },
  data() {
    return {
      username: '',
      email: '',
      password: '',
      loginErrorMessage: '',
      signUpErrorMessage: '',
      showSignUp: false,
    }
  },
  methods: {
    toggleSignUp() {
      this.showSignUp = !this.showSignUp;
    },
    async register_(username, email, password) {
      const response = await register(username, email, password);
      if (response.success) {
        this.signUpErrorMessage = ''; 
        this.$router.push('/home');
      } else {
        this.signUpErrorMessage = response.error;
      }
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

<style>
body {
  background: linear-gradient(to top, white, rgb(60 60 60 / 43%));
  margin: 0;
  height: 100%;
  width: 100%;
}
</style>