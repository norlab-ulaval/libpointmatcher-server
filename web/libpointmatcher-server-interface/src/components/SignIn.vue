<template>
    
    <div class="flex items-center justify-center min-h-screen ">
      <div class="relative w-96 max-w-md p-6 bg-white rounded-lg shadow-md">
        <div class="absolute left-1/2 transform -translate-x-1/2" style="top: -4rem;">
            <img src="/public/logo.png" alt="logo" class="h-24 w-24">
        </div>
        <form class="mt-10" @submit.prevent="handleSubmit">
          <h2 class="text-center text-3xl font-bold mb-6">Sign in</h2>
  
          <div class="mb-6">
            <label for="email" class="block text-lg font-medium text-gray-700">Email</label>
            <input type="text" id="email" v-model="email" @blur="validateEmail" 
            class="mt-2 block w-full px-4 py-3 border rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
            :class="[{'border-red-500': emailError, 'border-gray-300': !emailError}]" />
            <p v-if="emailError" class="mt-2 text-sm text-red-600">{{ emailError }}</p>
          </div>
  
          <div class="mb-8">
            <label for="password" class="block text-lg font-medium text-gray-700">Password</label>
            <div class="relative">
              <input :type="showPassword ? 'text' : 'password'" id="password" v-model="password" @blur="validatePassword" 
              class="mt-2 block w-full px-4 py-3 border rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
              :class="[{'border-red-500': passwordError, 'border-gray-300': !passwordError}]" />
              <div @click="showPassword = !showPassword" class="absolute inset-y-0 right-0 pr-3 flex items-center text-sm leading-5">
                <template v-if="showPassword">
                  <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 14c-.5-.6-.9-1.3-1-2 0-1 4-6 9-6m7.6 3.8A5 5 0 0 1 21 12c0 1-3 6-9 6h-1m-6 1L19 5m-4 7a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"/>
                  </svg>
                </template>
                <template v-else>
                  <svg class="w-6 h-6 text-gray-800 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <path stroke="currentColor" stroke-width="2" d="M21 12c0 1.2-4 6-9 6s-9-4.8-9-6c0-1.2 4-6 9-6s9 4.8 9 6Z"/>
                    <path stroke="currentColor" stroke-width="2" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"/>
                  </svg>
                </template>
              </div>
            </div>
            <p v-if="passwordError" class="mt-2 text-sm text-red-600">{{ passwordError }}</p>
          </div>
  
          <p v-if="loginError" class="error-message text-red-500">{{ loginError }}</p>
        
          <button type="submit" class="w-full px-5 py-3 font-bold text-white bg-black rounded-md text-lg hover:bg-gray-700">Sign in</button>
        </form>
  
        <p class="mt-6 text-center text-lg">
          Don't have an account yet?
          <a @click.prevent="showSignUp" class="text-black opacity-70 hover:text-gray-500 cursor-pointer">Sign up</a>
        </p>
      </div>
    </div>
  </template>
  

  <script>
  export default {
    props: {
        loginError: String,
    },
    data() {
      return {
        email: '',
        password: '',
        passwordError: '',
        emailError: '',
        showPassword: false,
      };
    },
    methods: {
      validateEmail() {
        const pattern = new RegExp('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$');
        this.emailError = pattern.test(this.email) ? '' : 'Please enter a valid email address.';
      },
      validatePassword() {
        this.passwordError = this.password.trim().length === 0 ? 'Password cannot be empty.' : '';
      },
      handleSubmit() {
        this.validateEmail();
        this.validatePassword();
        if (this.emailError || this.passwordError) {
          return;
        }
        this.$emit('login-event', this.email, this.password);
      },
      showSignUp() {
      this.$emit('toggle-signup');
      },
    }
  };
  </script>

