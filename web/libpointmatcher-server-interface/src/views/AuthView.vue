<template>
    <div class="bg-gradient-to-t from-neutral-400 to-slate-50 dark:bg-neutral-900 dark:bg-none">
        <ToastNotification :show="showToast" :message="toastMessage" />
        <SignIn @login-event="login_" :loginError="loginErrorMessage" v-if="!showSignUp" @toggle-signup="toggleSignUp" />
        <SignUp @signup-event="register_" :signUpError="signUpErrorMessage" v-else @back-to-signin="toggleSignUp" />
    </div>
  </template>
  
  <script>
  import SignIn from '../components/Auth/SignIn.vue';
  import SignUp from '../components/Auth/SignUp.vue';
  import ToastNotification from '../components/ui/ToastNotification.vue';
  import { register, login, logout } from '../api';
  import { useAuthStore } from '@/stores/authStore';
  
  export default {
    components: {
        ToastNotification,
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
        showToast: false,
        toastMessage: '',
      }
    },
    methods: {
      toggleSignUp() {
        this.showSignUp = !this.showSignUp;
        this.clearErrors();
      },
      async register_(username, email, password) {
        const response = await register(username, email, password);
        if (response.success) {
            this.signUpErrorMessage = ''; 
            this.showSignUp = false;
            this.displayToast('Account successfully created. Please sign in.');
        } else {
          this.signUpErrorMessage = response.error;
        }
      },
      async login_(email, password) {
        const response = await login(email, password);
        if (response.success) {
            this.loginErrorMessage = '';
            const authStore = useAuthStore();
            authStore.login(response.token);
            this.$router.push({ name: 'home'});
        } else {
            this.loginErrorMessage = response.error;
        }
      },
      async logout_() {
        await logout();
      },
      displayToast(message) {
        this.toastMessage = message;
        this.showToast = true;
        setTimeout(() => {
        this.showToast = false;
        }, 3000);
      },
        clearErrors() {
            console.log("Clearing errors");
            this.loginErrorMessage = '';
            this.signUpErrorMessage = '';
        },
    }
  };
  
  </script>
  
  <style>
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s;
  }
  .fade-enter-from, .fade-leave-to {
    opacity: 0;
  }
  </style>