<template>
    <div>
        <transition name="fade">
            <div v-if="showToast" class="fixed top-5 right-5 max-w-xs bg-white border border-gray-200 rounded-xl shadow-lg dark:bg-gray-800 dark:border-gray-700" role="alert">
                <div class="flex p-4">
                <div class="flex-shrink-0">
                    <svg class="flex-shrink-0 size-4 text-teal-500 mt-0.5" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>
                    </svg>
                </div>
                <div class="ms-3">
                    <p class="text-sm text-gray-700 dark:text-gray-400">
                    {{ toastMessage }}
                    </p>
                </div>
                </div>
            </div>
        </transition>
      <SignIn @login-event="login_" :loginError="loginErrorMessage" v-if="!showSignUp" @toggle-signup="toggleSignUp" />
      <SignUp @signup-event="register_" :signUpError="signUpErrorMessage" v-else @back-to-signin="toggleSignUp" />
    </div>
  </template>
  
  <script>
  import SignIn from '../components/SignIn.vue';
  import SignUp from '../components/SignUp.vue';
  import { register, login, logout } from '../api';
  
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
        showToast: false,
        toastMessage: '',
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
            this.showSignUp = false;
            this.displayToast('Account successfully created. Please sign in.');
        } else {
            console.log('erreur')
            console.log(response.error)  
          this.signUpErrorMessage = response.error;
          console.log(this.signUpErrorMessage)
        }
      },
      async login_(email, password) {
        const response = await login(email, password);
      if (response.success) {
        this.loginErrorMessage = '';
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
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s;
  }
  .fade-enter-from, .fade-leave-to {
    opacity: 0;
  }
  </style>