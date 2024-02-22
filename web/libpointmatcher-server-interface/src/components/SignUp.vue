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
            <input type="text" id="username" v-model="username" @blur="validateUsername"
            class="mt-2 block w-full px-4 py-3 border rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
            :class="[{'border-red-500': usernameError, 'border-gray-300': !usernameError}]" />
            <p v-if="usernameError" class="mt-2 text-sm text-red-600">{{ usernameError }}</p>
          </div>
  
          <div class="mb-4">
            <label for="email" class="block text-lg font-medium text-gray-700">Email</label>
            <input type="text" id="email" v-model="email" @blur="validateEmail" 
            class="mt-2 block w-full px-4 py-3 border rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
            :class="[{'border-red-500': emailError, 'border-gray-300': !emailError}]" />
            <p v-if="emailError" class="mt-2 text-sm text-red-600">{{ emailError }}</p>
          </div>
  
          <div class="mb-4">
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
          </div>
  
          <div class="mb-6">
            <label for="passwordConfirm" class="block text-lg font-medium text-gray-700">Confirm Password</label>
            <div class="relative">
              <input :type="showConfirmPassword ? 'text' : 'password'" id="passwordConfirm" v-model="passwordConfirm" @blur="validatePassword" 
              class="mt-2 block w-full px-4 py-3 border rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
              :class="[{'border-red-500': passwordError, 'border-gray-300': !passwordError}]" />
              <div @click="showConfirmPassword = !showConfirmPassword" class="absolute inset-y-0 right-0 pr-3 flex items-center text-sm leading-5">
                <template v-if="showConfirmPassword">
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
  
          <p v-if="signUpError" class="mt-2 text-sm text-center text-red-600">{{ signUpError }}</p>
          
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
        emailError: '',
        usernameError: '',
        showPassword: false,
        showConfirmPassword: false,
      };
    },
    methods: {
      validateUsername() {
        const pattern = new RegExp('.{2,}');
        this.usernameError = pattern.test(this.username) ? '' : 'Username must be at least 2 characters.';
      },
      validateEmail() {
        const pattern = new RegExp('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$');
        this.emailError = pattern.test(this.email) ? '' : 'Please enter a valid email address.';
      },
      validatePassword() {
        const pattern = new RegExp('^(?=.*[A-Z])(?=.*[a-z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$');
        if (!pattern.test(this.password)) {
          this.passwordError = 'Password must be at least 8 characters and include upper case, lower case, number, and special character.';
        } else if (this.password !== this.passwordConfirm) {
          this.passwordError = 'Passwords do not match.';
        } else {
          this.passwordError = '';
        }
      },
      showSignIn() {
        this.$emit('back-to-signin');
      },
      handleSubmit() {
        this.validateUsername();
        this.validateEmail();
        this.validatePassword();
        if (this.usernameError || this.emailError || this.passwordError) {
          return;
        }
        this.$emit('signup-event', this.username, this.email, this.password);
      }
    }
  };
  </script>
  