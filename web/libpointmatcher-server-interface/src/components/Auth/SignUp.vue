<template>
    <div class="flex items-center justify-center min-h-screen" style="padding-top: 10%;">
      <div class="relative w-96 max-w-md p-6 bg-white rounded-lg shadow-md dark:bg-neutral-700">
        <div class="absolute left-1/2 transform -translate-x-1/2" style="top: -4rem;">
            <img src="/public/logo.png" alt="logo" class="h-24 w-24">
        </div>
        <form class="mt-10" @submit.prevent="handleSubmit">
          <h2 class="text-center text-3xl font-bold mb-6 dark:text-gray-100">Sign up</h2>
  
          <div class="mb-4">
            <label for="username" class="block text-lg font-medium text-gray-700 dark:text-gray-200">Username</label>
            <input type="text" id="username" v-model="username" @blur="validateUsername"
            class="mt-2 block w-full px-4 py-3 border rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 dark:bg-neutral-600 dark:text-gray-200"
            :class="[{'border-red-500': usernameError, 'border-gray-300': !usernameError}]" />
            <p v-if="usernameError" class="mt-2 text-sm text-red-600">{{ usernameError }}</p>
          </div>
  
          <div class="mb-4">
            <label for="email" class="block text-lg font-medium text-gray-700 dark:text-gray-200">Email</label>
            <input type="text" id="email" v-model="email" @blur="validateEmail" 
            class="mt-2 block w-full px-4 py-3 border rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 dark:bg-neutral-600 dark:text-gray-200"
            :class="[{'border-red-500': emailError, 'border-gray-300': !emailError}]" />
            <p v-if="emailError" class="mt-2 text-sm text-red-600">{{ emailError }}</p>
          </div>
  
          <div class="mb-4">
            <label for="password" class="block text-lg font-medium text-gray-700 dark:text-gray-200">Password</label>
            <div class="relative">
              <input :type="showPassword ? 'text' : 'password'" id="password" v-model="password" @blur="validatePassword" 
              class="mt-2 block w-full px-4 py-3 border rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 dark:bg-neutral-600 dark:text-gray-200"
              :class="[{'border-red-500': passwordError, 'border-gray-300': !passwordError}]" />
              <div @click="showPassword = !showPassword" class="absolute inset-y-0 right-0 pr-3 flex items-center text-sm leading-5">
                <EyeSlashIcon v-if="showPassword"/>
                <EyeOpenIcon v-else/>
              </div>
            </div>
          </div>
  
          <div class="mb-6">
            <label for="passwordConfirm" class="block text-lg font-medium text-gray-700 dark:text-gray-200">Confirm Password</label>
            <div class="relative">
              <input :type="showConfirmPassword ? 'text' : 'password'" id="passwordConfirm" v-model="passwordConfirm" @blur="validatePassword" 
              class="mt-2 block w-full px-4 py-3 border rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 dark:bg-neutral-600 dark:text-gray-200"
              :class="[{'border-red-500': passwordError, 'border-gray-300': !passwordError}]" />
              <div @click="showConfirmPassword = !showConfirmPassword" class="absolute inset-y-0 right-0 pr-3 flex items-center text-sm leading-5">
                <EyeSlashIcon v-if="showConfirmPassword"/>
                <EyeOpenIcon v-else/>            
              </div>
            </div>         
            <p v-if="passwordError" class="mt-2 text-sm text-red-600">{{ passwordError }}</p>
          </div>
  
          <p v-if="signUpError" class="mt-2 text-sm text-center text-red-600">{{ signUpError }}</p>
          
          <button type="submit" class="w-full px-5 py-3 font-bold text-white bg-black rounded-md text-lg hover:bg-gray-700 dark:bg-gray-700 dark:hover:bg-gray-600">Sign up</button>

          <p class="mt-6 text-center text-lg dark:text-gray-200">
            Already have an account?
            <a @click.prevent="showSignIn" class="text-black opacity-70 hover:text-gray-500 cursor-pointer dark:text-gray-300 dark:hover:text-gray-100">Sign in</a>
         </p>
        </form>
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
        const pattern = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!"#$%&'()*+,-./:;<=>?@[\\\]^_`{|}~])[A-Za-z\d!"#$%&'()*+,-./:;<=>?@[\\\]^_`{|}~]{8,}$/;

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
    },
    beforeRouteLeave(to, from, next) {
      this.$emit('clear-errors');
      next();
    }
  };
  </script>
  
