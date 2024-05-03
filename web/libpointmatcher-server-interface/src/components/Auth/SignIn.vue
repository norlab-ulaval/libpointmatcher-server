<template>
    
    <div class="flex items-center justify-center" style="padding-top: 10%;">
      <div class="relative w-96 max-w-md p-6 bg-white rounded-lg shadow-md dark:bg-neutral-700">
        <div class="absolute left-1/2 transform -translate-x-1/2" style="top: -4rem;">
            <img src="/public/logo.png" alt="logo" class="h-24 w-24">
        </div>
        <form class="mt-10" @submit.prevent="handleSubmit">
          <h2 class="text-center text-3xl font-bold mb-6 dark:text-gray-100">Sign in</h2>
  
          <div class="mb-6">
            <label for="email" class="block text-lg font-medium text-gray-700 dark:text-gray-200">Email</label>
            <input type="text" id="email" v-model="email" @blur="validateEmail" 
            class="mt-2 block w-full px-4 py-3 border rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 dark:bg-neutral-600 dark:text-gray-200"
            :class="[{'border-red-500': emailError, 'border-gray-300': !emailError}]" />
            <p v-if="emailError" class="mt-2 text-sm text-red-600">{{ emailError }}</p>
          </div>
  
          <div class="mb-8">
            <label for="password" class="block text-lg font-medium text-gray-700 dark:text-gray-100">Password</label>
            <div class="relative">
              <input :type="showPassword ? 'text' : 'password'" id="password" v-model="password" @blur="validatePassword" 
              class="mt-2 block w-full px-4 py-3 border rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 dark:bg-neutral-600 dark:text-gray-200"
              :class="[{'border-red-500': passwordError, 'border-gray-300': !passwordError}]" />
              <div @click="showPassword = !showPassword" class="absolute inset-y-0 right-0 pr-3 flex items-center text-sm leading-5">
                <EyeSlashIcon v-if="showPassword"/>
                <EyeOpenIcon v-else/>   
              </div>
            </div>
            <p v-if="passwordError" class="mt-2 text-sm text-red-600">{{ passwordError }}</p>
          </div>
  
          <p v-if="loginError" class="mt-2 text-sm text-center text-red-600"> {{ loginError }}</p>
        
          <button type="submit" class="w-full px-5 py-3 font-bold text-white bg-black rounded-md text-lg hover:bg-gray-600 dark:bg-gray-700 dark:hover:bg-gray-600">Sign in</button>
        </form>
  
        <p class="mt-6 text-center text-lg dark:text-gray-200">
          Don't have an account yet?
          <a @click.prevent="showSignUp" class="text-black opacity-70 hover:text-gray-500 cursor-pointer dark:text-gray-300 dark:hover:text-gray-100">Sign up</a>
        </p>
      </div>
    </div>
  </template>
  

  <script>
  import EyeOpenIcon from '../icons/IconEyeOpen.vue'
  import EyeSlashIcon from '../icons/IconEyeSlash.vue'
  export default {
    components: {
      EyeOpenIcon,
      EyeSlashIcon,
    },
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
    },
  };
  </script>

