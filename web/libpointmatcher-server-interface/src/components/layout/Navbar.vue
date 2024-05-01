<template>
    <nav class="shadow w-full" style="background-color: #515151;">
        <div class="flex items-center justify-between px-10 py-2 mx-auto">

            <div class="pl-8">
                <router-link to="/home" class="inline-block p-0 m-0 align-middle">
                    <img src="/public/norlab_logo_acronym_light.png" alt="logo" class="h-auto" style="width: 11rem;">
                </router-link>                    
            </div>

            <div class="flex items-center mr-auto ml-8">
                <router-link
                    class="text-white border-b-2 border-transparent hover:border-white custom-text-size mr-8 pb-2 font-sans font-light"
                    to="/"
                    active-class="border-white"
                >
                    Home
                </router-link>
                <router-link
                    v-if="isLoggedIn"
                    class="text-white border-b-2 border-transparent hover:border-white custom-text-size mr-8 pb-2 font-sans font-light"
                    to="/uploads"
                    active-class="border-white"
                >
                    Uploads
                </router-link>
                <router-link
                    v-if="isLoggedIn"
                    class="text-white border-b-2 border-transparent hover:border-white custom-text-size pb-2 font-sans font-light"
                    to="/profile"
                    active-class="border-white"
                >
                    Profile
                </router-link> 
            </div>

            <div class="pr-8">
                <a v-if="isLoggedIn" class="text-white border-b-2 border-transparent hover:border-white custom-text-size font-sans pb-2 cursor-pointer font-light" @click="handleLogout">Log out</a>
                <router-link
                    v-if="!isLoggedIn"
                    class="text-white border-b-2 border-transparent hover:border-white custom-text-size pb-2 font-sans font-light"
                    to="/auth"
                    active-class="border-white"
                >
                    Log in
                </router-link>
            </div>
        </div>
    </nav>
</template>
  
  <script setup>
  import { onMounted } from 'vue';
  import { watchEffect } from 'vue';
  import { logout } from '@/api';
  import { authStore } from '@/stores/authStore';
  import { ref } from 'vue';

  const isLoggedIn = ref(false);

    const handleLogout = async () => {
        const result = await logout();
        if (result.success) {
            this.$router.push('/');
        } else {
            console.error(result.error);
        }
    }
//   export default {
//     name: 'Navbar',
//     methods: {
//         async handleLogout() {
//             const result = await logout();
//             if (result.success) {
//                 this.$router.push('/');
//             } else {
//                 console.error(result.error);
//             }
//         }
//     }
//   };
    onMounted(() => {
        authStore.checkAuth();
    });
    watchEffect(() => {
        console.log('Is logged in:', isLoggedIn);
    });
  </script>

<style>
.custom-text-size {
    font-size: 1.65rem;
}
</style>
  