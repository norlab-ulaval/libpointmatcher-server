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
            <input type="email" id="email" v-model="email" required class="mt-2 block w-full px-4 py-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500" />
          </div>
  
          <div class="mb-8">
            <label for="password" class="block text-lg font-medium text-gray-700">Password</label>
            <input type="password" id="password" v-model="password" required class="mt-2 block w-full px-4 py-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500" />
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
      };
    },
    methods: {
        handleSubmit() {
        this.$emit('login-event', this.email, this.password);
        },
        showSignUp() {
        this.$emit('toggle-signup');
        },
    }
  };
  </script>