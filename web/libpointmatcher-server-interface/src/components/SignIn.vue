<template>
    <div class="flex items-center justify-center min-h-screen ">
      <div class="w-full max-w-md p-8 bg-white rounded-lg shadow-md">
        <form>
          <div class="flex justify-center mb-8">
            <!-- Place your logo here -->
            <img src="/public/logo.png" alt="logo" class="h-16 w-16"> <!-- Logo plus grand -->
          </div>
  
          <h2 class="text-center text-3xl font-bold mb-6">Sign in</h2> <!-- Titre plus grand -->
  
          <div class="mb-6">
            <label for="email" class="block text-lg font-medium text-gray-700">Email</label>
            <input type="email" id="email" required class="mt-2 block w-full px-4 py-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500" />
          </div>
  
          <div class="mb-8">
            <label for="password" class="block text-lg font-medium text-gray-700">Password</label>
            <input type="password" id="password" required class="mt-2 block w-full px-4 py-3 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500" />
          </div>
  
          <button type="submit" class="w-full px-5 py-3 font-bold text-white bg-black rounded-md text-lg hover:bg-gray-700">Sign in</button>
        </form>
  
        <p class="mt-6 text-center text-lg">
          Don't have an account yet?
          <router-link to="/signup" class="text-black opacity-70 hover:text-gray-500">Sign up</router-link>
        </p>
      </div>
    </div>
  </template>
  

<!-- <script>
export default {
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    login() {
      this.$emit('login', this.user.email, this.user.password);
    }
  }
};
</script> -->

<style>
body {
  background: linear-gradient(to top, white, #CDCDCD);
  margin: 0;
  height: 100%;
  width: 100%;
}
</style>