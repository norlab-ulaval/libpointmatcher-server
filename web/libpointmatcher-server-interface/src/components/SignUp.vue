<template>
    <div class="flex items-center justify-center min-h-screen">
      <div class="relative w-96 max-w-md p-6 bg-white rounded-lg shadow-md">
        <div class="absolute left-1/2 transform -translate-x-1/2" style="top: -4rem;">
            <img src="/public/logo.png" alt="logo" class="h-24 w-24">
        </div>
        <form class="mt-10" @submit.prevent="handleSubmit">
          <h2 class="text-center text-3xl font-bold mb-6">Sign up</h2>
  
          <div class="mb-4">
            <label for="username" class="block text-lg font-medium text-gray-700">Username</label>
            <input type="text" id="username" v-model="username" required class="mt-2 block w-full px-4 py-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500" />
          </div>
  
          <div class="mb-4">
            <label for="email" class="block text-lg font-medium text-gray-700">Email</label>
            <input type="email" id="email" v-model="email" required class="mt-2 block w-full px-4 py-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500" />
          </div>
  
          <div class="mb-4">
            <label for="password" class="block text-lg font-medium text-gray-700">Password</label>
            <input type="password" id="password" v-model="password" required class="mt-2 block w-full px-4 py-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500" />
          </div>
  
          <div class="mb-6">
            <label for="passwordConfirm" class="block text-lg font-medium text-gray-700">Confirm Password</label>
            <input type="password" id="passwordConfirm" v-model="passwordConfirm" required class="mt-2 block w-full px-4 py-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500" />
          </div>
  
          <p v-if="passwordError" class="error-message text-red-500">{{ password }}</p>
          <p v-if="signUpErrorError" class="error-message text-red-500">{{ signUpError }}</p>
          
          <button type="submit" class="w-full px-5 py-3 font-bold text-white bg-black rounded-md text-lg hover:bg-gray-700">Sign up</button>

          <p class="mt-6 text-center text-lg">
            Already have an account?
            <a @click.prevent="showSignIn" class="text-black opacity-70 hover:text-gray-500 cursor-pointer">Sign in</a>
         </p>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
        signUpError: String,
    },
    data() {
      return {
        username: '',
        email: '',
        password: '',
        passwordConfirm: '',
        passwordError: '',
      };
    },
    methods: {
    showSignIn() {
      this.$emit('back-to-signin');
    },
      handleSubmit() {
        if (this.password !== this.passwordConfirm) {
          this.passwordError = "Passwords do not match.";
          return;
        }
        this.$emit('signup-event', { username: this.username, email: this.email, password: this.password });
      }
    }
  };
  </script>
  